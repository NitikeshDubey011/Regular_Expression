'''Question 4:  Write a Python program that matches a string that has an a followed by three 'b'. '''

import re
enter_string=str(input('> '))
if re.search('ab{3}',enter_string):
    print('Accepted!!')
else:
    print('Rejected!!')
