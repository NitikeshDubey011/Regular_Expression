import re


# ?! negative look ahead

# ?<! negative look behind

string = '''
Remaining party applicants:

Occupation: Party Planner
Occupation: Baking
Occupation: Cook
Occupation: Publicist
Occupation: Entertainer 
Occupation: Baker
Occupation: baker
Occupation: pierrot'''


# negative look ahead
patterns=re.compile('Occupation: (?!Baking|Cook|Baker).+', flags=re.IGNORECASE)
print(re.findall(patterns,string))

string2 = '''
Full invitation list:

Guest: Ashley Jackson
Guest: Maria Jackson
Guest: Bob Sanders
Guest: Bill Smith
Entertainer: Michael Johnson
Baker: Chris Jackson
Party Planner: Seema Patel
Publist: Seema Patel
Baker: Ashley Sanders'''

#negative look behind
pattern=re.compile(r'(?<!Baker: )\b\w+\s\w+$',flags=re.IGNORECASE|re.M)
print(re.findall(pattern,string2))

string3 = '''
Full invitation list:

Guest: Ashley Jackson
Guest: Maria Maria Jackson
Guest: Bob Sanders
Guest: Bill Smith Tom Josh
Entertainer: Michael Michael Johnson
Baker: Chris Jackson
Party Planner: Seema Patel
Publist: Seema Patel
Baker: Ashley Sanders'''


# pull out three full names or four fullnames
pattern2=re.compile(r'(?<!Baker: )(\b\w+\s\w+$|\b\w+\s\w+\s\w+$|\b\w+\s\w+\s\w+\s\w+$)',flags=re.IGNORECASE|re.M)
print(re.findall(pattern2,string3))


# pull out all the string except baker
patter3=re.compile(r'^(?!Baker: ).+\w+$',flags=re.IGNORECASE|re.M)
print(re.findall(patter3,string3))