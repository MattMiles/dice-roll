def parse_expression(expression):
    if not re.match('[1-9]+d[1-9]+', expression.lower()):
        print(expression, 'is not a valid expression.')
        return None
    else:
        result = re.findall('\d+', expression)
        num_of_dice = int(result[0])
        dice_sides = int(result[1])

        return num_of_dice, dice_sides

def main():
    expression = ''

    while expression != 'quit':
        expression = input('> ')
        dice_info = parse_expression(expression)
        if dice_info not None:
            roll(dice_info)
main()