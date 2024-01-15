#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard

import pyperclip
text = pyperclip.paste() # This is used to retrieve the content that is currently stored in the clipboard (The thing you copied before you ran the bat script)

# Seperate lines and add stars
lines = text.split('\n') # Makes a list of what was copied and all new line characters are returned as commas in the list
for i in range(len(lines)):  # loop through all indexed in the "lines" list
    lines[i] = '*' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines) # You are joining a new line to each index(commas) and the .join converts lists into string
print("Lines now have a *")

pyperclip.copy(text)

# This is what it is doing in simpler terms (remove the #)

#test = """Tyler
#Sigrid
#This is a test"""

#split_test = test.split('\n')

#print(split_test)

#combine = "\n".join(split_test)

#print(combine)