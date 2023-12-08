picnicItems = {'apples': 5, 'cups': 2}

print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 1)) + ' eggs.') # Because there is no egg key in the dictionary, the default value 1 is choosen instead.--