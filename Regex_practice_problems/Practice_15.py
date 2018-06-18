''' Write a Python program to check for a number at the end of a string. '''


import re
string=str(input('>'))
if re.search('.*[0-9]$',string):
    print('True')
else:
    print('False')