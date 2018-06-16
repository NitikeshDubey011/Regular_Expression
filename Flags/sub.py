import re

string = '''Here are the U.S stocks which are in news today:

Thomas Cook: The firm has granted options under the ESOP scheme 2018.

Punj Lloyd: The firm said that ICICI Bank has filed application before NCL under IBC code.

Blue Star USA: Company eyes 10 percent market share in water purifier business'''

print(re.sub('U.S|USA', 'United States', string))

print(re.sub('(\d+)', '1', string))
print()
square = lambda x: x ** 2
print(re.sub('(\d+)', lambda x: str(square(int(x.group(0)))), string))
str_data = 'James has 5 data and 15 cows also got feed by James.Jenny has 12 dogs.'

print('\n')
print(re.sub('(\d+)', lambda x: str(square(int(x.group(0)))), str_data))

input_data = 'eat laugh sleep study'
print(re.sub('\w+',lambda m:m.group(0)+"ing",input_data))


String_data='Merry Merry Christmas'
print(re.search(r'(\w+ )(\1)',String_data).groups())

print(re.search(r'(\w+ )(\1)',String_data).group(1,2))

temp=re.sub(r'(\w+) (\1)',r'Happy \1',String_data)
print(temp)

temp2=re.sub(r'(\w+) (\1)',r'\1 Happy',String_data)
print(temp2)