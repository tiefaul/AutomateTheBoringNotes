def spam(DivideBy):
    try:
        return 42 / DivideBy
    except ZeroDivisionError: # If this error occurs the code will still continue
        print("Error: Invalid argument")

print(spam(2))
print(spam(0))
print(spam(12))
print(spam(1))