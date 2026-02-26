print("Виртуальное окружение работает!")
import sys
print("Путь к Python", sys.executable)

print('Hello, world!')
print('What is your name?')  # ask for their name
type(len('Hello') == type(str))


myAge = 27

str(myAge + 1)

round(24.6654898, 2)

abs(-5.2)

name = input()
name

bacon = 20
bacon + 1

'spam' + 'spamspam'
'spam' * 3

int('100')
type(int(4))

quantity = '99'

'I eat ' + str(quantity) + ' burritos.'

bacon = 20
bacon + 1

bin(42)
hex(42)

spam = 9
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
 
print('Done')

True, False



if, elif, else 



 



False, False, True, False, False, True



==, >, <, >=, <=, !=



equal operator compares, assignment operator assign a value

spam = 0

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
print('Greetings!')

  a   |  b    | a or b | a and b | not a | not b 
 True | True  |  True  |  True   | False | False
 True | False |  True  |  False  | False | True
 False| True  |  True  |  False  | True  | False
 False| False |  False |  False  | True  | True
 
 
spam = 10
if spam == 10:
    print('eggs')
    if spam > 5:
       print('bacon')
    else:
        print('ham')
    print(spam)
print('Done')