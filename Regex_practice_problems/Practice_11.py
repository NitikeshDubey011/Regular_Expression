'''Question 11: Write a Python program that matches a word containing 'z' '''


import re
enter_string=str(input('> '))
if re.search('(?:z)+',enter_string):
    print('Found z.')
else:
    print('Not found z.')