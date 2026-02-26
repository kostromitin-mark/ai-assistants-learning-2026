# Here's my daily progress journal

## The 24 of February 2026
- created repository
- learned coouple commands in Powershell and git
- mood: OK

## my next step for today / tomorrow
- build easy bot in TG to undestand how some things work
- in this case I gonna ask LLM model for explanation how create tg bot without paid API

## The template of daily progress journal
Date: 25.02.26
Working time: 40 mins
What was done today: In my practice I learned about the sys module, I used string variable sys.executable

What didn't work / Where I got stuck: All good
Plan for today/ tomorrow: create easy echo bot 
Mood: OK
Notes / Insights:

Sys module it's built in module trough which Python "talks" with OS and himself
String variable sys.executable and it showed me path to the executable Python file


Date: 25.02.26
What was done today: In my practice I learned about the sys module, I used string variable sys.executable

What didn't work / Where I got stuck: All good
Plan for today/ tomorrow: created easy echo bot, next step - thinking trough the steps 
Mood: OK
Notes / Insights:

logging - It's record the events in special journal of logs (like file or console) while the programm is working.
I used it in echo_bot.py that bot can tell in console what's going on. 

Class Update used to represent incoming events from user (messages, commands, tapping of button)

Telegram.ext part of python-telegram-bot library where we can put essential tools (classes) for bot developing. For example:
Application - primary mechanism of coordinating all components in TG. All job builds around this object.
CommandHandler - catch messages starts from '/'. When user write a command starts with '/' it do the function. 
MessageHandler - listener for regular messages. It's function or class responds to incoming messages.
filters - list of filters. we could say to it which exact messages we need. For example filters.TEXT, filters.PHOTO, filters.COMMAND.
ContextTypes - techniqual thing which helps to indicate data types in functions correctly.

Date: 25.02.26
What was done today: Got a token from BotFather
Inserted a token to Python file
It's working and returns my messages 
Next step: protect a token before push it 


Date: 25.02.26
What didn't work / Where I got stuck: I stuck when tried to run command /help. I named file apifile.env instead of simple .env. That's why library python-dotenv didn't see it. 
What was done today: Renamed apifile.env to .env and now dotenv is reading BOT_TOKEN correctly 
Next step: Working on next bot

Date: 25.02.26
Good advice:
When asking for help, provide:
    What you are trying to achieve
    Exact error message
    Full code (use pastebin.com or gist.github.com)
    What you already tried
    Python version + operating system

What was done: I started to learn  https://automatetheboringstuff.com/ (next Python book) to understand how Python works while I'm working on telegram bots, I finished 1st part Python Basics
What didn't work / Where I got stuck: I failed 3 exercises

Note: After the test I should keep in mind that:

    -An expression is made up of values, operators, and possibly function calls (and parentheses). All expressions evaluate (reduce) to a single value.
    - adding of value does not change the variable unless you use assignment =
    - An expression evaluates to a single value, A statement is a complete instruction that does something

Plan for today/tomorrow: Explore 2nd chapter of Python book

Date: 26.02.26 
What was done: Learned 2nd chapter of Python book, completed exercises on understanding if-else and flow control
Next step: start to build telegram bot with CrewAI framework

