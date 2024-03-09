import re
def Pass_detection(pw):
    if len(pw) < 8:
       return False
    elif re.search('[0-9]|[A-Z]|[a-z]', pw) is None:
        return False
    else:
        return True

pw = input('Enter your password : ')
if Pass_detection(pw):
    print('Good, your password is strong!')
else:
    print('''
    The Password should at least be eight characters long,
    contains both uppercase and lowercase characters,
    and has at least one digit.
    ''') 