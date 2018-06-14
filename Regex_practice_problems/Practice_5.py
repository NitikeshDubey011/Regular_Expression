'''Question 5: Write a Python program that matches a string that has an a followed by two to three 'b'. '''
import re

enter_string=str(input('> '))
if re.search('ab{2,3}',enter_string):
    print('Accepted!!')
else:
    print('Rejected!!')
