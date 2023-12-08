birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'} # Dictionary containing birthdays (Alice, Bob, Carol, are all keys), and the dates are values

while True:
    print('Enter a name: (blank to quit)')
    name = input() # asking for a name for the user to input
    if name == '':
        break # breaks out of the loop and prints the dictionary

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name) # checks the birthdays dictionary for the key the user inputed and prints out the information if key matches.
    
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.') # User did not input a key that matched so the program asks for the key's bday and updates the dictionary with the new key


print(birthdays) # To show updated database after the break

# Note that these dictionaries do not save when terminating the code. Learn how to do that on chapter 9.