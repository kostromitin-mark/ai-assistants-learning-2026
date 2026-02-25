import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

from dotenv import load_dotenv
import os

load_dotenv()                  
TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text("Привет! Я эхо-бот. Напиши мне что-нибудь — я повторю.")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    await update.message.reply_text(update.message.text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text("Я эхо-бот \n/start - приветствие \n/help - помощь \nПросто пиши текст")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:

    logger.warning(f"Update {update} caused error {context.error}")
    
def main() -> None:

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.add_handler(CommandHandler("help", help_command))


    application.add_error_handler(error_handler)

    print("Бот запускается... (нажми Ctrl+C чтобы остановить)")

    application.run_polling(allowed_updates=Update.ALL_TYPES)
    


if __name__ == "__main__":
    main()