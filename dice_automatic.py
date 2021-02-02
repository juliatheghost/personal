import random

def roll(no_dice, dice_type):

    min = 1
    max = dice_type

    roll_again = 'yes'

    while roll_again == 'yes' or roll_again == 'y':

        print('Rolling...')
        print('The values are...')
        
        for i in range(no_dice):
            print(random.randint(min, max))

        roll_again = input('Roll_again?')
                  
