#How to use the TYPE function

name = "Tyler"
age = 24
decimal = 24.5 #Decimal numbers are called floating points

print(type(name))
print(type(age))
print(type(decimal))


#TYPE function shows the class of the code, whether its a str, int, etc

print(5 + 7) #Add
print(5 - 7) #Subtract
print(5 / 7) #Divide
print(5 * 7) #Multiply


#You can set math to a variable and print it out

math = 5 + 8
print(math)


#You can set variables to equations and then combine the equations into another variable for an outcome

add = 5 + 10
home = 1000
test = 5 / 7

print(add - home * test)


# Using += to add to an variable

x = 10 # Initialize a variable

x += 5 # Use the += operator to add a value to the variable (you can also do -= for subtraction)

print(x)  # Output: 15


#Lab using math

name = input("What is your name?\n")

print("Hello " + name + "!")

menu = "Pizza, Coffee, Taco"
price = 5

order = input("What would you like to eat?\n" + menu + "\n")

quantity = input("How many would you like?\n")

total = int(quantity) * price

print("Okay your price will be " + str(total) + (" dollars.\n"))

print(name + (" we will have your ") + str(quantity) + (" ") + ( order) + (" for you in a moment."))