# This program says hello and asks for your name

print("Hello, World!")
print("What is your name?") # ask for their name

myname = input()

print("It is good to meet you, " + myname)
print("The length of your name is:")
print(len(myname))

print("What is your age?") # ask for their age

myage = input()

print("You will be " + str(int(myage) + 1) + " in a year.") 
