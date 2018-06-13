import re

# we can name the group by using ?P<> by this syntax.For example: ?P<Name>,?P<City>, etc.


dataInVar = 'New York,New York 133456'
# search and print the matched group
match_data = re.search('([A-Za-z\s]+),([A-Za-z\s]+) (\d+)', dataInVar)
print(re.search('([A-Za-z\s]+),([A-Za-z\s]+) (\d+)', dataInVar))
print()
print(match_data.group(1), match_data.group(2), match_data.group(3), match_data.group())

var_data=re.compile('(?P<City>[A-Za-z\s]+),(?P<State>[A-Za-z\s]+)(?P<Zipcode>\d+)')
match=re.search(var_data,dataInVar)
print(match.group('City'))
print(match.group('State'))
print(match.group('Zipcode'))


# if you forgot the name of the groups you chose earlier
print(match.groupdict())