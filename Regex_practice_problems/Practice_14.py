'''Question 14:  Write a Python program where a string will start with a specific number. '''

import re
enter_string=str(input('> '))
if re.search('^[0-9]',enter_string):

    print('Condition Satisfied.')
else:
    print('Condition Not Satisfied.')
