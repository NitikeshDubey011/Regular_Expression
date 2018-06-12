import re

# "\w" is used to matches alpha numeric character [a-zA-Z0-9_]

print(re.search('\w\w\w\w', 'abcdef'))

# output: <_sre.SRE_Match object; span=(0, 4), match='abcd'>
# only four chars printed because I use only '\w' four times
'''output has span(0,4) and match is 'abcd' span is the index of the characters 
i.e. abcd has occurred from index 0 and ended at index 4'''

# 'r' in front of \w\w is used to create the string to raw string
print(re.search(r'\w\w\w', 'absdfghjkl'))
# output: <_sre.SRE_Match object; span=(0, 3), match='abs'>

print(re.search('\w\w\w\w', 'abc_defg'))
# output: <_sre.SRE_Match object; span=(0, 4), match='abc_'>

'''output contains '_' underscore because it falls under [a-zA-Z0-9_] condition'''

print(re.search('\w\w\w\w\w', 'abc_.3df'))
# output: None
# output is None because it is not falling under given condition.'.' is not in the condition

print(re.findall('\w\w\w\w','abcdef'))
# findall condition with \w
