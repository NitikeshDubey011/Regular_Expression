import re

# string
stringData = "Data is easy to get."
# search a from given string

# search is used to search the data from anywhere in the sentence
# span(1,2) is the index of the occurrence of the words i.e. 'a' is occurred at index 1 and end at index at 2
print(re.search('a', stringData))

# group() is used to get the text
print()
print(re.search('Data', stringData).group())
# or
print(re.search('is', stringData).group(0))
# above statements are same


# match is used to find the first character from the sentence

print(re.match('D',stringData).group(0))

# produce None because t is not found at first character
print(re.match('t',stringData))


# start() is used to print first index
print(re.search('s',stringData).start())

# end() is used to print end index
print(re.search('s',stringData).end())

