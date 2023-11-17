while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue #allows the above while statement to continue 
    print("Hello Joe. What is the password?")
    password = input()
    if password == 'swordfish':
        break   #This statement allows the next print statement to be executed, exiting the while loop
print('Access Granted')