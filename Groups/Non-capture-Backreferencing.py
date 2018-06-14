import re

String_data = '1234 56789'

print(re.findall('(\d)+', String_data))
print(re.search('(\d)+', String_data).groups())

# non-capture groups syntax
# ?: - Symbol for non-capture group, this is used to find the occurrence of the words
# ?P - Symbol for naming groups

print(re.findall('(\d)+', String_data))

print(re.findall('(?:\d)+', String_data))
string = '123123 = Alex, 123123123 = Danny, 123123123123 = Mike, 456456 = rick, 121212 = John, 132132 = Luis,'

String = "123=Darek, 123123=Samuels, 456123=Danis, 456456=Roy,"
print(re.findall('(?:123)+=(\w+),', String))

str_val = "486=Jake, 485486745586=Daniel, 486486=Mikesss,"
print(re.findall('(?:486)+=(\w+),', str_val))

string_val = '1*1*1*1*22222 1*1*1*33333 2*1*2*1*22222 1*1*2222*2*23333 1*1*1*3*3*4444'
# to extract the data  from the upper string
print(re.findall(r'(?:3\*){2,}\d+', string_val))

data_string = 'Merry Merry Christmas, You You are are very happy to check it check out out.'
# this will find find all repeated words and representing as one word
print(re.findall(r'(\w+) \1', data_string))

# this will find only one occurrence and stop searching
print(re.search(r'(\w+) \1', data_string))

# this will find repeated words group
# output has only one group beacause we're using search
print(re.search(r'(\w+) \1', data_string).groups())
