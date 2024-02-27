#! python3

import pyperclip, re

phoneNumbers = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?              # Area code
                        (\s|-|\.)?                      # separator
                        (\d{3})                         # first 3 digits
                        (\s|-|\.)                       # separator
                        (\d{4})                         # last 4 digits 
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extenstion
                        )''', re.VERBOSE)

findEmail = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+      # Username
                        @                      # @ symbol
                        [a-zA-Z0-9.-]+         # domain name 
                        (\.[a-zA-Z]{2,4})        # dot-something
                        )''', re.VERBOSE)

# Find matches in clipboard text

text = str(pyperclip.paste())

matches = []
for groups in phoneNumbers.findall(text):
    phonenum =  '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phonenum += ' x' + groups[6]
    matches.append(phonenum)

for groups in findEmail.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')