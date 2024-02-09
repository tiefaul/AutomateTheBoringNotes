import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # Creating groups within regex
mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups()) # list out all the groups

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

print()

pipe = re.compile(r'Batman|Spiderman') # this will match either batman or spiderman
pipe1 = pipe.search('Batman or Spiderman') # searches for either batman or spiderman, whichever comes first will be what is printed.
print(pipe1.group())

print()

theres = re.compile(r'The(re|ir|y\'re)') # how to specify a prefix 
search = theres.search("They're in the trees")
print(search.group())
print(search.group(1)) # prints out matched text inside the first parentheses group

print()
"""MATCHING WITH QUESTION MARKS"""

batRegex = re.compile(r'Bat(wo)?man') # The question mark flags the group that precedes it as an optional part of the pattern
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

print()
"""Matching Zero or More with the Star"""

batRegex2 = re.compile(r'Bat(wo)*man') # The group that precedes the star can occur any number of times in the text.
mo3 = batRegex2.search('The Adventures of Batwowowowoman')
print(mo3.group())

print()
"""Matching Specific Repetitions with Braces"""
haRegex = re.compile(r'(Ha){3}') # Setting "3" to "1,3" will return Ha, HaHa, or HaHaHa if searched
ha = haRegex.search('HaHaHa')
print(ha.group())

print()
"""Greedy and Non-Greedy Matching"""
# Add a ? mark to the code above to bring out the shortest string possible
nongreedyHa = re.compile(r'(Ha){3,5}?')
ngha = nongreedyHa.search('HaHaHaHaHa')
print(ngha.group()) # Without the ? mark 5 HaHa would have been printed out because it has the most occuring characters

print()
"""The findall() Method"""
 
number = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
num = number.search('Cell: 415-555-9999 Work: 123-456-7890')
print(num.group())

allnum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(allnum.findall('Cell: 415-555-9999 Work: 123-456-7890'))
