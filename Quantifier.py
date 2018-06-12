# some required knowledge '+' =1 or more
# '?' = 0 or 1
# '*' = 0 or more
# '{n,m}' = n to m repetitions(ranges)


import re

testData='The quick brown fox jumps over the lazy dog'

# to get the data from the start
print(re.search('\w+',testData).group())
# output:The

# \W+ will get the space and \w+ will print the next characters
print(re.search('\w+\W+\w+',testData).group())
# output:The quick


# little bit extended version of  upper data
print(re.search('\w+\W+\w+\W+\w+\W+\w+',testData).group())
# output:The quick brown fox

# \W+ got all the spaces but \W? will get 0 or 1 space
print(re.search('\w+\W?\w+',testData).group())
# output:The quick

testData2='The quick  brown fox'
print(re.search(r'\w+\W?\w+\W+\w+',testData2).group())
# output: The quick  brown

testData3='Thee quick  brown fox'
# prints the first three characters
print(re.search(r'\w{3}',testData3).group())
# output: The


# prints the first three chars from 0 index to 3 index(excluding)
print(re.search(r'\w{0,3}',testData3).group())
# output: The


# we can use this
print(re.search(r'\w{0,4}\W{0,5}\w+',testData3).group())
# output: Thee quick
