# '\d' = matches digits[0-9]
# '\D' = This matches any non digit character
# '\s' = This matches any white space character (new lines, tabs, spaces etc.)
# '\S' = This matches non white space character
# '.' = This is used to match any character except newline
# '[A-Z] = contains all the capital letter in a list
# '[a-z] = contains all the small letter in a list


import re

string = 'Introd231uction'

print(re.search('\d+', string).group())
# this is used to get the digits from the string
# output: 231

# using \D to find only string character from a variable
print(re.search('\D+', string).group())
print()

# using \D and \w collectively
print(re.search('\D+\w+', string).group())
print()


data_in_string='''Python is an interpreted high-level programming language for general-purpose programming. 
Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, 
notably using significant whitespace.'''


# by this method we got all the words without spaces into a list.
print(re.findall('\S+',data_in_string))
print()

# by this method we join all the characters from a string.
print(' '.join(re.findall('\S+',data_in_string)))
print()

# print all the characters except newline
print(re.search('.+',data_in_string).group())
print()

# we learned the syntax in the basics.py file, till now we haven't used flag parameter
# but now we will use flag. Flag is used a special option in regex
print(re.search('.+',data_in_string,flags=re.DOTALL).group())
print()


# looking in data_in_string variable there are total five characters which are in capital letters
# expected output 'P', 'C', 'G', 'R', 'P'
print(re.findall('[A-Z]',data_in_string))


# output will contains '.'
print(re.findall('[A-Z.]',data_in_string))

# output will contains ',' and '.'
print(re.findall('[A-Z.,]',data_in_string))

# looking in data_in_string variable there are many characters which are in small letters
print(' '.join(re.findall('[a-z]',data_in_string)))

dataSet="Hello, There, is data in Two variable."
# to get all the spaces,commas, small letter and capital letters
print(re.findall('[A-Za-z,\s.]',dataSet))