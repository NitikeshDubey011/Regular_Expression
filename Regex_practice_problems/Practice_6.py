'''Question 6: Write a Python program to find sequences of lowercase letters joined with a underscore. '''

import re

enter_string=str(input('> '))
if re.search('^[a-z]+_[a-z]+$',enter_string):
    print('Its a match!!')
else:
    print('Not a match!!')
