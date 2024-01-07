'Hello, World!'.startswith('Hello') # Prints True because the string starts with Hello

'abc123'.endswith('12') # Prints False because it ends with 23 not 12

', '.join(['cats', 'rats', 'bats']) # Prints cats, rats, bats as a string

'ABC'.join(['My', 'name', 'is', 'Simon']) # Prints MyABCnameABCisABCSimon

'My name is Simon'.split() # Creates a list ['My', 'name', 'is', 'Simon'], turns the string into a list.

'MyABCnameABCisABCSimon'.split('ABC') # Creats a list, just removes ABC (if there were spaces, it would keep the spaces, because you specified a different delimiter)

'Hello, world!'.partition('w') # This creates the Tuple ('Hello, ', 'w', 'orld!') seperates the strink w from everything else
# If the seperator string you pass occurs multiple times, then the first occurance appears.

before, sep, after = 'Hello, world!'.partition(' ') # You can assign variables to the partitions, Before prints Hello, After prints world!, Sep prints the space

'Hello'.rjust(10) # Pushes hello 5 spaces to the right. The 10 is the total length + the string (.ljust will push 5 spaces to the left)

'Hello'.rjust(20, '*') # This will add 15 '*' to the left of Hello (.ljust will add the '*' to the right)

'Hello'.center(20, '=') # This will center the string Hello in between 15 '='
