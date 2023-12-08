import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count) # Prettifies the text to make it easier to read.

print('')

print(pprint.pformat(count)) # Used to obtain the prettified text as a string value. 