dic = {'Name': 'Tyler', 'Size': 'Tall', 'Age': 42}

print(dic['Size']) # Prints out the Key(Size) and prints the value(Tall)

print('')

for i in dic.values(): # List all the values in the dictionary
    print(i)

print('')

for i in dic.keys(): # List all the keys in the dictionary 
    print(i)

print('')

for i in dic.items(): # List all the items in the dictionary and their pairs
    print(i)

print('')

print(list(dic.keys())) # Converts the dictionaries key values into a list

print('')


for i, v in dic.items(): # Using a for loop to assign the key and value to separate variables
    print('Key: ' + i + ', Value: ' + str(v))