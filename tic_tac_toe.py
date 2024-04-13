
def game_setup(player):
    valid_symbol = False
    player1_symbol = None
    player2_symbol = None

    print(f"This is numeration of the board:\n"
          f"| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n"
          f"{player} starts first!\n")

    while not valid_symbol:
        symbol = input(f"{player1} would you like to play with 'X' or 'O'?:")
        if symbol == 'X' or symbol == 'x' or symbol == 'O' or symbol == 'o':
            valid_symbol = True
            if symbol == 'X' or 'x':
                player1_symbol = 'X'
                player2_symbol = 'O'
            else:
                player1_symbol = 'O'
                player2_symbol = 'X'
        else:
            print('Please, enter a valid symbol!')
            continue
    return player1_symbol, player2_symbol


def choose_position(player, mapp):
    valid_position = False
    position = None
    while not valid_position:
        try:
            position_check = int(input(f"{player}, please choose a free position [1-9]:"))
            if 0 < position_check <= 9:
                position = position_check
                if board[mapp[str(position)][0]][mapp[str(position)][1]] != ' ':
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print('Please enter a number between 1 and 9 and make sure it is not taken.')
            continue
        else:
            valid_position = True
    return position


def draw_map(board):
    b = ''
    for row in board:
        line = '|' + '    ' '|'.join(row) + '    ' + '|'
        b += f'{line}\n'
    return b


def play(player_position, curr_symbol, mapp):
    player_position = str(player_position)
    board[mapp[player_position][0]][mapp[player_position][1]] = curr_symbol
    b = ''
    for row in board:
        line = '| ' + ' | '.join(row) + ' |'
        b += f'{line}\n'
    return b


def check_winner(curr_symbol, board):
    if any(all(cell == curr_symbol for cell in row) for row in board):
        return True
    if any(all(row[i] == curr_symbol for row in board) for i in range(3)):
        return True
    if all(board[i][i] == curr_symbol for i in range(3)) or all(board[i][2 - i] == curr_symbol for i in range(3)):
        return True
    return False


player1 = input(f'Player one name: ')
player2 = input(f'Player two name: ')
board = [[' ' for col in range(3)] for row in range(3)]
player_one_symbol, player_two_symbol = game_setup(player1)
winner = False
turn = 0
turn_counter = 0

mapper = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (2, 0), '8': (2, 1), '9': (2, 2)}

while not winner:
    starting_player = player1 if turn % 2 == 0 else player2

    if starting_player == player1:
        current_symbol = player_one_symbol
    else:
        current_symbol = player_two_symbol

    position = choose_position(starting_player, mapper)
    print(play(position, current_symbol, mapper))

    if turn == 8:
        print('Tie !!')
        winner = True

    if check_winner(current_symbol, board):
        print('\033[31m' + f'{starting_player} won !!')
        winner = True
    turn += 1
