''' Write a Python program to find the occurrence and position of the substrings within a string.'''
import re

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
matching=re.finditer(pattern,text)
for i in matching:
    start_d=i.start()
    end_d=i.end()
    print('The occurrence %s at %d:%d' %(text[start_d:end_d],start_d,end_d))