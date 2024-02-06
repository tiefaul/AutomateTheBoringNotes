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