'''  Write a Python program to replace whitespaces with an underscore and vice versa. '''
import re

inp_val=str(input('> '))
pattern=re.sub('\s+','_',inp_val)
print(pattern)

#or
print('\n***********Second method***********\n')
pattern_=inp_val.replace(" ","_")
print(pattern)
pattern_2=inp_val.replace("_"," ")
print(pattern_2)