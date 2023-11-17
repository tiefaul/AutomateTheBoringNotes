import random, sys

print("Rock, Paper, or Scissors")

wins = 0
loss = 0
tie = 0

# These variables keep track of the number of wins, losses, and ties.

while True: # Main game loop
    print('%s Wins, %s loss, %s tie' % (wins, loss, tie)) 
    while True: # Player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playermove = input()
        if playermove == 'q':
            sys.exit() # Quit program
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break # Break player out of the input loop
        print('Type one of r, p, s, or q.')
    
    # Display what the player chose

    if playermove == 'r':
        print('ROCK versus...')
    elif playermove == 'p':
        print('PAPER versus...')
    elif playermove == 's':
        print('SCISSORS versus...')
    
    # Display what the computer chose
    randomnumber = random.randint(1,3)
    computermove = ''
    if randomnumber == 1:
        computermove = 'r'
        print('ROCK')
    if randomnumber == 2:
        computermove = 's'
        print('SCISSORS')
    if randomnumber == 3:
        computermove = 'p'
        print('PAPER')

    # Display Win, Loss, Tie record
    if playermove == computermove:
            print('It is a tie!')
            tie = tie + 1
    elif playermove == 'r' and computermove == 's':
            print('You win!')
            wins = wins + 1
    elif playermove == 's' and computermove == 'p':
            print('You win!')
            wins = wins + 1
    elif playermove == 'p' and computermove == 'r':
            print('You win!')
            wins = wins + 1
    elif playermove == 'r' and computermove == 'p':
            print('You lose!')
            loss = loss + 1
    elif playermove == 'p' and computermove == 's':
            print('You lose')
            loss = loss + 1
    elif playermove == 's' and computermove == 'r':
            print('You lose')
            loss = loss + 1