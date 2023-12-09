# How to print out character count including " " (Spaces)

count = 0
message = 'This is a test'

for i in message:
    if i == ' ':
        count += 1
    else:
        count += 1

print(count)

# How to use isspace and isalpha

count = 0
message = 'This is a test'

for i in message:
    if i.isspace:
        count += 1
    elif i.isalpha:
        count += 1

print(count)

# Both codes do the same thing
