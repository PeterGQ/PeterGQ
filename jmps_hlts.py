"""
    Come up with a name for the game

    JMPs and HLTs
"""

import random

GRID_WIDTH = 8
GRID_HEIGHT = 3
DICE_SIDES = 6


def generate_random_map(length, the_seed=0):
    """
        :param length - the length of the map
        :param the_seed - the seed of the map
        :return: a randomly generated map based on a specific seed, and length.
    """
    if the_seed:
        random.seed(the_seed)
    map_list = []
    for i in range(length - 2):
        random_points = random.randint(1, 100)
        random_position = random.randint(0, length - 1)
        map_list.append(random.choices(['nop', f'add {random_points}', f'sub {random_points}', f'mul {random_points}', f'jmp {random_position}', 'hlt'], weights=[5, 2, 2, 2, 3, 1], k=1)[0])

    return ['nop'] + map_list + ['hlt']
def make_grid(table_size):
    """
    :param table_size: this needs to be the length of the map
    :return: returns a display grid that you can then modify with fill_grid_square (it's a 2d-grid of characters)
    """
    floating_square_root = table_size ** (1 / 2)

    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_height = int_square_root
    if int_square_root * (int_square_root - 1) >= table_size:
        table_height -= 1

    the_display_grid = [[' ' if j % GRID_WIDTH else '*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        if i % GRID_HEIGHT else ['*' for j in range(GRID_WIDTH * int_square_root + 1)]
                        for i in range(table_height * GRID_HEIGHT + 1)]
    return the_display_grid


def fill_grid_square(display_grid, size, index, message):
    """
        :param display_grid:  the grid that was made from make_grid
        :param size:  this needs to be the length of the total map, otherwise you may not be able to place things correctly.
        :param index: the index of the position where you want to display the message
        :param message: the message to display in the square at position index, separated by line returns.
        """
    floating_square_root = size ** (1 / 2)
    int_square_root = int(floating_square_root) + (1 if floating_square_root % 1 else 0)
    table_row = index // int_square_root
    table_col = index % int_square_root
    if table_row % 2 == 0:
        column_start = GRID_WIDTH * table_col
    else:
        column_start = GRID_WIDTH * (int_square_root - table_col - 1)

    for r, message_line in enumerate(message.split('\n')):
        for k, c in enumerate(message_line):
            display_grid[GRID_HEIGHT * table_row + 1 + r][column_start + 1 + k] = c
def roll_dice():
    """
        Call this function once per turn.

        :return: returns the dice roll
    """
    return random.randint(1, DICE_SIDES)

def get_score(roll, val, count):
    # does all the calculations/ get the score
    if (roll == "add"):
        return count + val
    elif (roll == "mul"):
        return count * val
    elif (roll == "sub"):
        return count - val
    else:
        return count

def display_board(rand_, grid):
    # displays the board in the correct format
    for x in range(len(rand_)):
        filler_line = "\n"
        info = str(x) + filler_line + rand_[x]
        fill_grid_square(grid, size, x, info)

    for i in grid:
        print(''.join(i))

def jump(position, spot):
    """
    """
    # sets the integer next to jmp as the current position
    position = spot
    return position

def play_game(game_map):
    """
    :param game_map:
    :return:
    """

    real_grid = make_grid(size)
    a_grid = generate_random_map(size, the_seed)
    b_grid = len(a_grid)
    display_board(a_grid, real_grid)
    score = 0
    position = 0
    roll = 0
    playing = True
    while game_map[position] != "hlt":
        if playing == True:
            roll = roll_dice()
            # sets the position to the roll of the dice
            position += roll
            position = position % b_grid
        spot = a_grid[position].split()
        spot_ = a_grid[position].strip("'[]',")
        spot_1 = spot[0]
        comma = ','
        print("Pos:",position,"Score:",str(score) + comma,"instruction",spot_,"Rolled:",roll)
        # checks if the first part of the phrase in that position is mul, sub, or add
        if (spot_1 == 'mul') or (spot_1 == 'add') or (spot_1 == 'sub'):
            spot_2 = int(spot[1])
            score = get_score(spot_1, spot_2, score)
            # print(score(score, roll, spot_2))
            playing = True
        # checks if the first part of the phrase in the position is jmp then makes the integer the current position
        elif spot_1 == 'jmp':
            spot_2 = int(spot[1])
            position = jump(position, spot_2)
            position = position % b_grid
            playing = False
        else:
            playing = True
    comma = ','
    print("Final Pos:", position, "Final Score:", str(score) + comma,"Instruction", spot_)
if __name__ == '__main__':
    Bool = True
    while Bool != False:
        numbers = input('Enter the dimensions (and optionally the seed): ').split(" ")
        num = numbers
        # splits the user input into 2 parts. the size and the seed
        size = int(numbers[0])
        the_seed = int(numbers[1])
        play_game(generate_random_map(size, the_seed))
        Input = input("Would you like to play again?").lower()
        if Input == "yes":
            Bool == True
        else:

            print("have a good day")
            Bool = False


