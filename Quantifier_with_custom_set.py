import re

string_var = 'You, are, AWESOME!.'

# it will find all the capital letter words and char from a string
print(re.findall('[A-Z]+', string_var))

string_var_sec = 'YOU, are, AWESOME!.'

# it will find capital letter words and char from a string
print(re.findall('[A-Z]{2,}', string_var_sec))

string_var_thi = 'You., are.., AWESOME!.'

# it will find all the words containing small letters,capital letters, commas
print(re.search('[A-Za-z\s,]+', string_var_thi).group())
# output: You
# the output is only you because after you there is dot and we excluded this

# it will find all the words containing small letters,capital letters, commas,exclamatory and fullstop.
print(re.search('[A-Za-z\s,.!]+', string_var_thi).group())
print(re.findall('[A-Z]?[A-Za-z\s,.!]', string_var_sec))

''' there is a new metacharacter i.e. '^'
using it outside the [] barckets means including and using it inside the
[] brackets means excluding the condition's character'''
print(re.findall('[^A-Za-z\s,.]', string_var_thi))
# only output value will be '!'

# it will print only lowercase letters from a string
print(re.findall('[^A-Z]+',string_var_thi))

