import random
import re

def parse_expression(expression):
    ''' 
        Parses the expression given by the user. Returns the
        number of dice and the number of sides on each die.
    '''
    if not re.match('[1-9]+d[1-9]+', expression.lower()):
        print(expression, 'is not a valid expression.')
        return None
    else:
        result = re.findall('\d+', expression)
        num_of_dice = int(result[0])
        dice_sides = int(result[1])

        return num_of_dice, dice_sides

def roll(num_of_dice, dice_sides):
    '''
        Rolls "num_of_dice" dice with "dice_sides" sides.
    '''

    dice_sum = 0
    for i in range(num_of_dice):
        current_roll = random.randint(1, dice_sides)
        print('\tRolling 1d' + str(dice_sides) + '...', current_roll)
        dice_sum += current_roll
    
    if num_of_dice > 1:
        print('TOTAL:', dice_sum, '/', num_of_dice * dice_sides)

def main():
    expression = ''

    while expression != 'quit':
        expression = input('> ')
        dice_info = parse_expression(expression)
        if dice_info is not None:
            num_of_dice = dice_info[0]
            dice_sides = dice_info[1]
            roll(num_of_dice, dice_sides)
main()