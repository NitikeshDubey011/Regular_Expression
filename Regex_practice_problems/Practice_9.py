'''Question 9: Write a Python program that matches a word at the beginning of a string. '''

import re
enter_string=str(input('> '))
if re.match('^North\.?',enter_string):
    print('Same!')
else:
    print('Not as same!!')