''' Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. '''

import re
stri=str(input('> '))
if re.finditer(r'([0-9]{1,3})',stri):
    for n in re.finditer(r'([0-9]{1,3})',stri):
        print(n.group(0))
else:
    print('Not Found!!')
