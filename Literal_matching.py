import re

testString = 'This is text for test the data'
# to search 'n' or 'a' (which occurred first)
print(re.search('n|a', testString).group())

# to search 'n' or 'a' or 't' or 'd' (which occurred first)
print(re.search('n|a|t|d', testString).group())

# to find all 't' or 'T' (occurred in the string)
print(re.findall('t|T', testString))

# to find all 'This' (occurred in the string)
print(re.findall('This', testString))

testData = 'You all know we gonna learn everything. You all are awesome'

# to find all 'You' or 'all' in the string
print(re.findall('You|all',testData))
