import re

str_var = 'abababababab'
print(re.search('(ab)+', str_var))
print()
print(re.search('[ab]+', str_var))

str2 = 'abababbbbbbbb'
print(re.search('(ab)+', str2))
print()
print(re.search('[ab]+', str2))
match = re.search('(ab)+', str_var)
match2 = re.search('(ab)+(ab)+', str_var)
print(match)
print()
# it will give the first group what we've created
print(match.group(1))
print(match.groups())

# it will give error of IndexError because we have created only one group
print(match2.group(2))

# it will give all the groups
print(match2.groups())

# printing index of all groups
print(match2.span(1))

var_num = '123456789'
matches = re.search('(\d)+', var_num)
print(re.search('(\d)+', var_num).group())
print(matches.groups())

data_string = '123456789'
print(re.findall('(\d)+', data_string))

data_string_data = '1234 56789'
print(re.findall('(\d)+', data_string_data))

print(re.findall('((\d)+)', data_string_data))

# slices 
data_in = re.findall('((\d)+)', data_string_data)[0][0]
print(data_in)

d = 'abbbbb abababababab'
print(re.findall('(ab)+', d))

print(re.findall('((ab)+)', d))

# Groups for word completion
print(re.search('Happy (Valentines|Birthday|Anniversary)', 'Happy Valentines'))
