'''Question 12: Write a Python program that matches a word containing 'z', not start or end of the word. '''
import re
enter_string=str(input('> '))
if re.search('\Bz\B',enter_string):
    print('Found z.')
else:
    print('Not found z.')