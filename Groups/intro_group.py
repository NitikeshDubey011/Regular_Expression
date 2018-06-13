# groups are used to pull out the specific group of data from string
# in groups which is denoted by '()' pulls out only grouped condition's data if it is applied to the query
import re

string = 'John has 6 cats but i think my friend Susan has 3 Dogs and Mike has 7 fishes.'
print(re.findall('[A-Za-z]+ \w+ \d+ \w+', string))
# Output: ['John has 6 cats', 'Susan has 3 Dogs', 'Mike has 7 fishes']
# there is Uppercase and lowercase containing words, one word, one digit and last word as it satisfies the condition


# as I mentioned above only grouped condition prints the value and all the query was neglected
print(re.findall('([A-Za-z]+) \w+ \d+ \w+', string))

# lets play with groups
# name of animals
print(re.findall('[A-Za-z]+ \w+ \d+ (\w+)', string))

# digital values
print(re.findall('[A-Za-z]+ \w+ (\d+) \w+', string))
print(re.findall('[A-Za-z]+ (\w+) \d+ \w+', string))
print(re.findall('([A-Za-z]+) (\w+) \d+ \w+', string))

variable = re.findall('([A-Za-z]+) \w+ (\d+) (\w+)', string)

'''The zip() function take iterables (can be zero or more), 
makes iterator that aggregates elements based on the 
iterables passed, and returns an iterator of tuples.'''
print(list(zip(*variable)))

# it will print the first occurrence of the group
variable2 = re.search('([A-Za-z]+) \w+ (\d+) (\w+)', string)
print(variable2)

print(variable2.group(0))
print(variable2.groups())
print(variable2.group(1))
print(variable2.group(2))
print(variable2.group(3))
print(variable2.group(3, 1))
print(variable2.group(3, 2, 2, 1))

# now lets take the subgroups
print(re.findall('(([A-Za-z]+) \w+ (\d+) (\w+))', string))
# output: [('John has 6 cats', 'John', '6', 'cats'), ('Susan has 3 Dogs', 'Susan', '3', 'Dogs'), ('Mike has 7 fishes', 'Mike', '7', 'fishes')]
# the output is first full string and then 3 different elements of the group

data = re.findall('(([A-Za-z]+) \w+ (\d+) (\w+))', string)
for i in data:
    print(i[1:3])


# now we are using iteration
data=re.finditer('([A-Za-z]+) \w+ (\d+) (\w+)',string)
print(next(data).group())

for i in data:
    print(i.group())