from board import Board

def select_position(board):
    valid = False
    while not valid:
        try:
            result = input("row,col: ").split(',')
            row = int(result[0])
            col = int(result[1])
            if not board.valid_position(row, col):
                raise ValueError
            valid = True
        except:
            print("Invalid position")
    return row, col

def start_game(num_rows=10, num_columns=10, num_bombs=8):
    board = Board(num_rows, num_columns, num_bombs)
    failed = False
    while board.remaining_available_positions() > 0 and not failed:
        board.print_dug_places_board()
        row, col = select_position(board)
        if not board.dig(row, col):
            failed = True
        print()
    if not failed:
        print("You won!!!")
        board.print_dug_places_board()
    else:
        print("You lost!!!")
        board.print_complete_board()

start_game(num_rows=5, num_columns=5, num_bombs=2)
