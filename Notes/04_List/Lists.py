spam = ['cat', 'dog', 'mouse']

print(spam[0] + '\n') # prints cat

print('Next list example \n')

combined_list = [[1, 10, 21, 15], ['cat', 'dog', 'mouse']]

print(combined_list[0][1]) # prints 10
print(combined_list[1][0]) # prints cat
print(combined_list[0]) # prints out the first list
print(combined_list[1]) # prints out second list
print('')
print('Next example: slicing \n')

# This is an example of slicing

slice = ['cat', 'dog', 'mouse']

print(slice[0:2]) # Prints out cat and dog, leaves out mouse because slicing includes every number but the last.
print(slice[:2]) # Prints list without mouse
print(slice[1:]) # Excludes cat (0)
print(slice[:]) # Prints entire list
print('')
print('Next example: Changing lists \n')

replace_list = ['Tyler', 'Steve', 'Justin']
print(replace_list)

replace_list[1] = 'Robert' # Replaces Steve with Robert
print(replace_list)

replace_list[1] = replace_list[0] # Replaces Steve (1) with Tyler (0)
print(replace_list) 

replace_list = replace_list * 3 # List out the list 3 times
print(replace_list)

replace_list = replace_list + [1, 2, 3] # adds 1,2,3 to the list
print(replace_list) 

del replace_list[2] # del Removes Justin
print(replace_list)

# append(), extend(), remove(), sort(), reverse() These are the types of list methods you can use