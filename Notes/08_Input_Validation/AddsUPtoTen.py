import pyinputplus as pyip

def addsUpToTen(numbers):
    numberslist = list(numbers)
    for i, digit in enumerate(numberslist):
        numberslist[i] = int(digit) # converts the numbers in the list to an integer and adds them back in the list
    if sum(numberslist) !=10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numberslist))) # percent sign is the sum of the list, and you have to define the percent sign at the end of the statement
    return int(numbers)

response = pyip.inputCustom(addsUpToTen)