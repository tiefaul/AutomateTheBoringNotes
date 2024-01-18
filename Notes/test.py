# Blank sheet for me to test things

print('Enter the English message to translate into Pig Latin:')
message = input()

Vowels = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of the words in Pig Latin
for word in message.split():
    print(word)