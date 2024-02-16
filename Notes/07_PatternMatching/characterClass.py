import re

xmasRegex = re.compile(r'\d+\s\w+') # '\d+\s\w+' will match one or more numberic (\d+) followed by whitespace characters (\s) and then one or more letter/digit/underscore characters (\w+)
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

print()
"""Making your own character classes"""

vowelRegex = re.compile(r'[aeiouAEIOU]') # this defines your own character class using the square brackets, [a-zA-Z0-9] will match all lowercase, upper, and numbers
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

print()
"""Negative class character"""
consonantRegex = re.compile(r'[^aeiouAEIOU]') # '^'after the bracket, means find every number,space,letter,etc, except for the ones listed.
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD'))

print()
"""Caret and Dollar sign characters"""

beginWithHello = re.compile(r'^Hello') # ^ at the start of the regex means that a match must occur at the beginning of the searched text.
print(beginWithHello.search('Hello, world!'))
print(beginWithHello.search('He said hello.')== None) # True because 'hello' was not at the beginning.
print()
endsWithNumber = re.compile(r'\d$') # Dollar sign means "ends with" so it is looking for a digit at the end of the search
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.') == None)

print()
"""Wild Card Character"""
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))
