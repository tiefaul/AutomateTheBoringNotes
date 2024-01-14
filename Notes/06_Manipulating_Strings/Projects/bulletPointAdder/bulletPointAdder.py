#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# Seperate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):  # loop through all indexed in the "lines" list
    lines[i] = '*' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
print("Lines now have a *")

pyperclip.copy(text)