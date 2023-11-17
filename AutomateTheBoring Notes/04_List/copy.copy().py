import copy

spam = ['A', 'B', 'C', 'D']
print(id(spam)) # id shows the memory byte that your computer picks

cheese = spam
print(id(cheese)) # notice how this id is the same as spam (Whatever is changed on the list changes both)

print(spam)
print(cheese)

cheese = copy.copy(spam)
print(id(cheese)) # Creates a new id because cheese is now its own list

cheese[0] = 'Hello'

print(spam)
print(cheese)