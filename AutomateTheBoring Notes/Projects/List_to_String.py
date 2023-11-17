# This code takes a list and prints it into a string while adding a ',' and a 'and' at the end of the list.

def str_list(list_name):
    if not list_name:
        return ""
    elif len(list_name) == 1:
        return list_name[0]
    else:
        return ', '.join(list_name[:-1]) + ', and ' + list_name[-1]
    
spam = ['apples', 'bananas', 'tofu', 'cats']
result = str_list(spam)
print(result)
