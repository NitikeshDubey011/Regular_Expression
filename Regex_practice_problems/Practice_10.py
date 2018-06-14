'''Question 10: Write a Python program that matches a word at end of string, with optional punctuation. '''

import re

enter_string=str(input('> '))
if re.match('\w+\S*$',enter_string):
    print('Same!')
else:
    print('Not same!!')