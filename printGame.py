# A game that prints according to user input.

import random, sys

print('Please enter 1, 2, or anything else:')
spam = int(input())
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
