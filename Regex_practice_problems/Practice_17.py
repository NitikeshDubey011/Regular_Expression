''' Write a Python program to find the substrings within a string'''
import re

stri = 'Python exercises, PHP exercises, C# exercises'
pattern = re.findall('exercises', stri)
for rou in pattern:
    print(rou)
