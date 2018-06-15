# in this practice set we are going to use split
import re

string = 'Today environment is not very clear. Dust is in the air.'
print(re.split('\.', string))
print(re.split('(\.)', string))
split = '.'
print([i + split for i in re.split('\.', string)])
str_var = '<p>My mother has <span style="color:blue">blue</span> eyes.</p>'
print(re.split('<\.+>',str_var))
print(re.split('<\.+>',str_var))
print(re.split('<.+>',str_var))
print(re.split('<[^<>]+>',str_var))