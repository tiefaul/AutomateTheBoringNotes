spam = 'Hello, world!'
spam = spam.upper() # Converts all text to uppercase
print(spam)

print('')

spam = spam.lower() # Converts all text to lowercase
print(spam)

print('')

print('How are you?')
feeling = input()
if feeling.lower() == 'great': # This makes it to where even if the user types GREAT or GReat, the if statement will still be true as long as they spell great correctly. 
    print('I feel great too')
else:
    print('I hope the rest of your day is good')
