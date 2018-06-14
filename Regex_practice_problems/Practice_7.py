'''Question 7: Write a Python program to find sequences of one upper case letter followed by lower case letters. '''

import re

enter_string=str(input('> '))
if re.search('^[A-Z]{1}[a-z]+$',enter_string):
    print('Its a match!!')
else:
    print('Not a match!!')
