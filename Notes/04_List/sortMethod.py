list = ['Tyler', 'Adam', "Steve"]

list.sort() # Sorts the list in alphabetical order, it does the same for numbers 
print(list)

list.sort(reverse=True) # sorts the list from Z-A, does the same for numbers or you can use list.reverse()
print(list)

print('')

# The sort method does NOT sort numbers and strings. Also it sorts uppercase letters before lowercase letters
# To sort uppercase and lowercase together, do the following below

uplower = ['tyler', 'Tyler', 'Adam', 'adam', 'steve', 'Steve']

uplower.sort()
print(uplower)

uplower.sort(key=str.lower)
print(uplower)
