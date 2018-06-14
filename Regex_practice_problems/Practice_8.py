'''Question 8: Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'. '''

import re

enter_string=str(input('> '))
if re.search('^(a)+[A-Za-z0-9@!#$%^&*)(;]+(b)+$',enter_string):
    print('Its a match!!')
else:
    print('Not a match!!')
