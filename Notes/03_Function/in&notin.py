List = ['Tyler', 'Tim', 'Steve']

print('What are the names of my dogs?')

while True:
    dogName = input('Dog name: ')
    if dogName not in List: # Also can use "in" instead of "not in" just does the opposite.
        print('I do not have a dog named ' + dogName + '.')
    else:
        print('Yes that is one of the names')
    
