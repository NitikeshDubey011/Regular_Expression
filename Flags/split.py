# in this practice set we are going to use split
import re

string = 'Today environment is not very clear. Dust is in the air.'
print(re.split('\.', string))
print(re.split('(\.)', string))
split = '.'
print([i + split for i in re.split('\.', string)])
str_var = '<p>My mother has <span style="color:blue">blue</span> eyes.</p>'
print(re.split('<\.+>',str_var))

# this is used to capture anyrthing
print(re.split('<.+>',str_var))
# this is same as above query
print(re.split('<[^<>]+>',str_var))

# removing spaces from a string
temp=[i for i in re.split('<[^<>]+>',str_var) if i!='']
print(temp)

# alternative option to split
print(re.findall('>([^<]+)<',str_var))

# The other method to get rid of the spaces is filter and list
temp_str=',happy, birthday,'
temp2=list(filter(None,temp_str.split(',')))
print(temp2)

