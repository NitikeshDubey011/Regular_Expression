'''Question 1:  Write a Python program that matches a string that has an a followed by zero or more b's'''

import re

enter_string=str(input('> '))
if re.search('ab*?',enter_string):
    print('Found a match!')
else:
    print('Not matched!!')
