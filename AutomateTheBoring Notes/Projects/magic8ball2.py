import random

messages = ['It is certain',
            'it is decidedly so',
            'reply hazly, try again',
            'ask again later',
            'answer is yes',
            'answer is no']

print(messages[random.randint(0, len(messages) - 1)]) # This allows messages from -1 and above to be displayed

#message = random.choice(messages)
#print(message) # This allows all the messages in the list to be printed out