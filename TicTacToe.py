# Power to the player! Enjoy.
indexes = list('         ')
possible_moves = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']
legal_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def build_board():
    print('-' * 9)
    print(f'| {indexes[0]} {indexes[1]} {indexes[2]} |')
    print(f'| {indexes[3]} {indexes[4]} {indexes[5]} |')
    print(f'| {indexes[6]} {indexes[7]} {indexes[8]} |')
    print('-' * 9)


def player_one():
    move = input('Enter the coordinates: ')
    if move[0:] not in legal_characters and move[2] not in legal_characters:
        print('You should enter numbers!')
        player_one()
    elif move not in possible_moves:
        print('Coordinates should be from 1 to 3!')
        player_one()
    elif move == '1 1' and indexes[6] != 'X' and indexes[6] != 'O':
        indexes[6] = 'X'
    elif move == '1 2' and indexes[3] != 'X' and indexes[3] != 'O':
        indexes[3] = 'X'
    elif move == '1 3' and indexes[0] != 'X' and indexes[0] != 'O':
        indexes[0] = 'X'
    elif move == '2 1' and indexes[7] != 'X' and indexes[7] != 'O':
        indexes[7] = 'X'
    elif move == '2 2' and indexes[4] != 'X' and indexes[4] != 'O':
        indexes[4] = 'X'
    elif move == '2 3' and indexes[1] != 'X' and indexes[1] != 'O':
        indexes[1] = 'X'
    elif move == '3 1' and indexes[8] != 'X' and indexes[8] != 'O':
        indexes[8] = 'X'
    elif move == '3 2' and indexes[5] != 'X' and indexes[5] != 'O':
        indexes[5] = 'X'
    elif move == '3 3' and indexes[2] != 'X' and indexes[2] != 'O':
        indexes[2] = 'X'
    else:
        print('This cell is occupied! Choose another one!')
        player_one()


def player_two():
    move = input('Enter the coordinates: ')
    if move[0:] not in legal_characters and move[2] not in legal_characters:
        print('You should enter numbers!')
        player_two()
    elif move not in possible_moves:
        print('Coordinates should be from 1 to 3!')
    elif move == '1 1' and indexes[6] != 'X' and indexes[6] != 'O':
        indexes[6] = 'O'
    elif move == '1 2' and indexes[3] != 'X' and indexes[3] != 'O':
        indexes[3] = 'O'
    elif move == '1 3' and indexes[0] != 'X' and indexes[0] != 'O':
        indexes[0] = 'O'
    elif move == '2 1' and indexes[7] != 'X' and indexes[7] != 'O':
        indexes[7] = 'O'
    elif move == '2 2' and indexes[4] != 'X' and indexes[4] != 'O':
        indexes[4] = 'O'
    elif move == '2 3' and indexes[1] != 'X' and indexes[1] != 'O':
        indexes[1] = 'O'
    elif move == '3 1' and indexes[8] != 'X' and indexes[8] != 'O':
        indexes[8] = 'O'
    elif move == '3 2' and indexes[5] != 'X' and indexes[5] != 'O':
        indexes[5] = 'O'
    elif move == '3 3' and indexes[2] != 'X' and indexes[2] != 'O':
        indexes[2] = 'O'
    else:
        print('This cell is occupied! Choose another one!')
        player_two()


def winner():
    wins = [indexes[:3], indexes[3:6], indexes[6:], indexes[0:9:3], indexes[1:9:3], indexes[2:9:3], indexes[0:9:4],
            indexes[2:7:2]]
    if "'X', 'X', 'X'" in str(wins):
        print('X wins')
        return True
    elif "'O', 'O', 'O'" in str(wins):
        print('O wins')
        return True


def main_game():
    build_board()
    while True:
        player_one()
        build_board()
        if indexes.count(' ') == 0 and winner() is not True:
            print('Draw')
            break
        if winner() is True:
            break
        player_two()
        build_board()
        if indexes.count(' ') == 0 and winner() is not True:
            print('Draw')
        if winner() is True:
            break


main_game()