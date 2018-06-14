'''Question 13: Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores. '''


import re
enter_string=str(input('> '))
if re.search('^[A-Za-z0-9_]*$',enter_string):

    print('Condition Satisfied.')
else:
    print('Condition Not Satisfied.')
