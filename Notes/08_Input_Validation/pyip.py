import pyinputplus as pyip # writing "as pyip" makes it to where it shortens pyinputplus to pyip so you are not typing out the whole name when coding

FloatnNumbers = pyip.inputNum(prompt='Enter float or number: ') # This will output numbers and floats (prompt= is optional)
Numonly = pyip.inputInt('Enter a number only: ') # This will only output numbers and NOT floats

"""min, max, greaterThan, and lessThan keyword Arguments"""

minimum = pyip.inputNum('Enter number that is at least 4: ', min=4) # The number must me a minimum of 4
greaterThan = pyip.inputNum('Enter number that is greater than 4: ', greaterThan=4) # Number must be greater than 4
lessthan = pyip.inputNum('> ', min=4, lessThan=6) # Number must be between 4 and 6..... making the answer 54 
# Putting blank=true in the inputNum statement will allow blank answers

"""The limit, timeout, and default keyword arguments"""
trylimit = pyip.inputNum('You have two tries: ' , limit=2)
timelimit = pyip.inputNum('You will be timed out in 10 seconds: ', timeout=10)

"""The allowRegexes and blockRegexes Keyowrd Arguments"""
allowRoman = pyip.inputNum('Enter Roman Numeral: ', allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

