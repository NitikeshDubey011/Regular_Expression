# alphanumeric characters = \w [A-Za-z0-9_]
# non alpha numeric character = \W +:@^%
# it is important here to learn about \b->\b don't consider nonalphanumeric character as character it skips that word
# space is also a non alpha numeric character
import re

string = 'cat catherine catholic wildcat copycat uncatchable'

pattern = re.compile('cat')
print(re.findall(pattern, string))

temp = re.compile('cat ')
print(re.findall(temp, string))

temp2 = re.compile(r'\bcat\b')
print(re.findall(temp2, string))

# this example gives the brief about \b
temp_data = '.cat. catherine catholic wildcat copycat uncatchable'
# it count the cat because it skips the non alphanumeric
temps = re.compile(r'\bcat\b')
print(re.findall(temps, temp_data))

temp_data2 = '.@cat@ catherine catholic wildcat copycat uncatchable'
# it count the cat because it skips the non alphanumeric
temps2 = re.compile(r'\bcat\b')
print(re.findall(temps2, temp_data2))

list_name = ['@nitikeshdubey', '@rakesh', '@robert_downey', 'iron@ironman']
pattern = re.compile(r'\B@[\w]+\b')
print(re.search(pattern, list_name[2]))
