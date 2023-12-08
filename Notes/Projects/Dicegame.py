import random

while True:
    input('Press any key to roll the dice!')

    randomroll = random.randint(1,12)

    print('You rolled a' , randomroll)
    input('Roll again.')

    secondrandomroll = random.randint(1,12)
    
    print('You rolled a ' + str(secondrandomroll) + '.')
    print('Your total score is ' + str(randomroll + secondrandomroll) + '.')