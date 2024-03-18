import pyinputplus as pyip

while True:
    question = pyip.inputYesNo('Would you like to know how to keep an idiot busy for hours? ')
    if question == 'no':
        print('Thank you. Have a nice day.')
        break

    # question = pyip.inputYesNo('Would you like to know how to keep an idiot busy for hours? ', yesVal='si', noVal='no') # This can be used to change the yes and no into different languages
    # if question == 'no':
    #     print('Thank you. Have a nice day.')
    #     break