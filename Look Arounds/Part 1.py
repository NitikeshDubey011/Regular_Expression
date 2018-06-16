# some required knowledge

'''

Positive look around= ?=
negative look around= ?!
positive look behind= ?<=
negative look behind=?<!

# similar syntax

?: non capturing group
?P naming groups

'''
import re
string='''ABC1      1.1.1.1     2017166     active
          ABC2      2.2.2.2     2017166     inactive
          ABC3      x.x.x.x     2017166     active'''

pattern=re.compile('ABC\w\s+(\S+)\s+\S+\s+(?=active)')
print(re.findall(pattern,string))
# the above used condition is not captured while printing the output because it is just a condition
print(re.search(pattern,string))

# by this example you will understand
_pattern=re.compile('ABC\w\s+(\S+)\s+\S+\s+(?:active)')
print(re.findall(_pattern,string))
print(re.search(_pattern,string))

# difference between  non capture groups and look arounds
str_data='abababacb'
pattern_=re.compile('(?:b)(a)(?:b)')
print(re.findall(pattern_,str_data))

# in the above example we found a surround by b but not included 'a'

str_data_2='abababacb'
pattern_2=re.compile('(?<=b)(a)(?=b)')
print(re.findall(pattern_2,str_data_2))


# look ahead
str2='I love  cherries, apples, and strawberries.'
pattern_data=re.compile(r'(\w+)(?=\.|,)')
print(re.findall(pattern_data,str2))


pattern_data=re.compile(r'(\w+)(?:\.|,)')
print(re.findall(pattern_data,str2))



