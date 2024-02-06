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

pipe = re.compile(r'Batman|Spiderman') # this will match either batman or spiderman
pipe1 = pipe.search('Batman or Spiderman') # searches for either batman or spiderman, whichever comes first will be what is printed.
print(pipe1.group())