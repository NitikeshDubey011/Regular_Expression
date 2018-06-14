''' flags are used as parameter and they are used in
re.match, re.search, re.findall. They are used a addition options in regular expressions.


^(carat sign) = this is used to find the match at the beginning of the string
$(Dollar sign) = this is used to find the match at the ending of the string'''

import re

news_data='''Paytm sale: 20 gadgets to buy in less than Rs 1,000
Telecom war fallout: RCom workforce down 94%
Israel: Indian-origin woman running for mayor post
Sanjay Dutt to watch his biopic post its release
A great course medical students can pursue
Here's how India is becoming a Land of Innovation
SC refuses to stay UPPSC mains exam
Muslim model loses job for wearing hijab
B'luru’s burqa market blooms with Arabian wares
Nirav Modi 'flees UK on muslim Singapore passport'
J&K: BSF officer hugged dad, martyred soon after'''


# using of carat prints the output None because Land is not in the start
print(re.search('^Land\.?',news_data))
# using of carat prints the output None because Land is not in the start(using of carat and match is same.)
print(re.match('Land\.?',news_data))
# using of dollar sign prints the output because after is in the end
print(re.search('after\.?$',news_data))

# now coming flags
# re.MULTILINE/re.M = This feature give the addition capacity to the carat to look for instances of each line of the string
# it only works with re.search but not worked with re.match
print(re.search('^Muslim\.?',news_data,flags=re.MULTILINE))


# next flag is re.IGNORECASE/re.I
# this will help to get the word by ignoring the cases.

print(re.findall('Muslim',news_data,flags=re.I))

# re.DOTALL is used to read the full paragraph including newline
print(re.match('.*',news_data).group())
print(re.match('.*',news_data,flags=re.DOTALL).group())