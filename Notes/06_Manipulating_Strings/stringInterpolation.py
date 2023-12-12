name = 'Tyler'
age = 25

print('My name is %s. I am %s years old.' % (name, age)) # %s is string interpolation in which it acts as a marker to be replaced by following the string.

print('')

print(f'My name is {name}. Next year I will be {age + 1}.') # This is a f string, notice the f before the string. Must use braces.
