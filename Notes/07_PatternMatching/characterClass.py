import re

xmasRegex = re.compile(r'\d+\s\w+') # '\d+\s\w+' will match one or more num eric (\d+) followed by whitespace characters (\s) and then one or more letter/digit/underscore characters (\w+)
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
atRegex = re.compile(r'.at') # looks for words that end in at 
print(atRegex.findall('The cat in the hat sat on the flat mat'))

print()
"""Matching Everything with Dot-Star"""
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Tyler Last Name: Faulhaber')
print(mo.group(1)) # Prints Tyler
print(mo.group(2)) # Print Faulhaber

"""Regex Symbols

The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets. """

print()
"""Case-Insensitive Matching"""
robocop = re.compile(r'robocop', re.I) # re.I is for ignore cases.
print(robocop.search('RoBoCop is part man, machine, and cop.'))

print()
"""Spread Regular Expressions"""
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)