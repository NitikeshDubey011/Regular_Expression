import re

string = '''1111    ABCC    77777777    active
           2222    ABC     88888888    inactive
           3333    XYZ     xxxxxxxx    active
           4444    1234    20351118    inactive  
           5555    1445    20153318    inactive  
           '''

# pattern = re.compile('(?<=[A-Z]+)[A-Z]+\s+(\S+)')
# print(re.findall(pattern, string))
# above code will give the following error
# sre_constants.error: look-behind requires fixed-width pattern

# so we have to perform above action by different way

import regex

# this code will give proper result
pattern = regex.compile('(?<=[A-Z]+)[A-Z]+\s+(\S+)')
print(regex.findall(pattern, string))


s= 'C:\Tools\System32\calc.exe'
s2= 'C:\Windows\System32\calc.exe'
s3= 'C:\Windows\System32\De-de\calc.exe'
s4= 'C:\Tools\calc.exe'


pattern_=regex.compile(r'(?<!System32.*)calc.exe')
print(regex.findall(pattern_,s4))