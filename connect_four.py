from pyfiglet import figlet_format


ROWS = 6
COLS = 7

possible_directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]

matrix = [[0 for col in range(COLS)] for row in range(ROWS)]


def check_valid_column(selected_column):
    return 0 <= selected_column <= COLS


def check_boundary(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS


def check_position(current_row, current_col, row_movement, col_movement, matrix, player):
    count = 1
    for i in range(1, 4):
        row_index_to_check = current_row + row_movement * i
        col_index_to_check = current_col + col_movement * i
        if not check_boundary(row_index_to_check, col_index_to_check):
            break
        if matrix[row_index_to_check][col_index_to_check] != player:
            break
        count += 1
    return count


def check_opposite_position(current_row, current_col, row_movement, col_movement, matrix, player):
    count = 0
    for i in range(1, 4):
        row_index_to_check = current_row - row_movement * i
        col_index_to_check = current_col - col_movement * i
        if not check_boundary(row_index_to_check, col_index_to_check):
            break
        if matrix[row_index_to_check][col_index_to_check] != player:
            break
        count += 1
    return count


def is_winner(current_row, current_col):
    for row_movement, col_movement in possible_directions:
        count_position = check_position(current_row, current_col, row_movement, col_movement, matrix, player)
        count_opposite_position = check_opposite_position(current_row, current_col, row_movement, col_movement, matrix, player)
        if count_position + count_opposite_position >= 4:
            return True
    return False


def draw_player(column, matrix, player):
    col = column - 1
    valid_column = False
    current_row = None
    while not valid_column:
        for row in range(ROWS - 1, -1, -1):
            if matrix[row][col] == 0:
                matrix[row][col] = player
                valid_column = True
                current_row = row
                break
            elif matrix[row][col] != 0 and row == 0:
                print(f'Player {player}, please enter a different column')
                col = int(input()) -1
    for row in matrix:
        print(row)
    return current_row


turn = 1
while True:
    player = 1 if turn % 2 != 0 else 2
    try:
        player_input = int(input(f'Player {player}, please choose a column: '))
        if not check_valid_column(player_input):
            print(f'Number must be between 1 and {COLS}')
            continue
    except ValueError:
        print(f'Number must be between 1 and {COLS}')
        continue

    else:
        curr_row = draw_player(player_input, matrix, player)
        column = player_input - 1
        if is_winner(curr_row, column):
            print(figlet_format(f'W I N NE R !'))
            print('\033[31m' + f'Player {player} wins !')
            exit()

    turn += 1
