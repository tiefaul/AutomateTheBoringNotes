name = ''  
while not name:  
    print('Enter your name')
    name = input()
print('How many guests will you have?')

numOfGuests = int(input())

if numOfGuests:
    print('Be sure to have enough room for all your guests.')

print('Done')

#If the user enters a blank string for name, then the while statement’s condition will be True and the program continues to ask for a name. 