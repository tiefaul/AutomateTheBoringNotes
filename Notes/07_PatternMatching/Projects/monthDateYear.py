import re

date = re.compile(r'''(
                  (\d\d)/   # Day
                  (\d\d)/ # Month
                  (\d{1,5}) # Year
                  )''', re.VERBOSE)

inputdates = '30/06/2024, 03/03/3000, 28/02/1998'

for groups in date.findall(inputdates):
     
    if (int(groups[2]) == 4  or int(groups[2]) == 6 or int(groups[2]) == 9 or int(groups[2]) == 11) and int(groups[1]) > 30: # Verifies that April, June, September, November don't go over 30 days
        print('Not valid', end=': ')

    elif int(groups[2]) == 2 and int(groups[1]) > 28: # Verifies that Feburary doesn't go over 28 days
        print('Not valid', end=': ')
    
    elif int(groups[3]) < 1000 or int(groups[3]) > 2999: # Validates that the year is within a certain range
        print('Not valid', end=': ')
    
    else:
        print('This is a valid date', end=': ')

    print(f'{groups[1]}/{groups[2]}/{groups[3]}')