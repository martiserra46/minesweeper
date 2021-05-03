import random as rd

class Board:
    def __init__(self, num_rows=10, num_columns=10, num_bombs=8):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.num_bombs = num_bombs
        self.bomb_positions = set()
        self.dug_positions = set()
        self.board = [[0 for j in range(num_columns)] for i in range(num_rows)]
        self.place_bombs()
        self.assign_numbers_to_cells()
        
    def place_bombs(self):
        for i in range(self.num_bombs):
            row, col = None, None
            while row is None or col is None or self.board[row][col] != 0:
                row, col = rd.randint(0, self.num_rows - 1), rd.randint(0, self.num_columns - 1)
            self.board[row][col] = '*'
            self.bomb_positions.add((row, col))
    
    def assign_numbers_to_cells(self):
        for (bomb_row, bomb_col) in self.bomb_positions:
            for i in range(bomb_row - 1, bomb_row + 2):
                for j in range(bomb_col - 1, bomb_col + 2):
                    if self.valid_position(i, j) and self.board[i][j] != '*':
                        board_value = self.board[i][j]
                        self.board[i][j] += 1

    def print_dug_places_board(self):
        dug_places_board = [[self.board[i][j] if (i, j) in self.dug_positions else ' ' for j in range(self.num_columns)] for i in range(self.num_rows)]
        for row in dug_places_board:
            row = [str(value) for value in row]
            print('| ' + ' | '.join(row) + ' |')

    def print_complete_board(self):
        for row in self.board:
            row = [str(value) for value in row]
            print('| ' + ' | '.join(row) + ' |')
    
    def dig(self, row, col):
        if (row, col) in self.bomb_positions:
            return False
        if (row, col) in self.dug_positions:
            return True
        self.dug_positions.add((row, col))
        if self.board[row][col] == 0:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if self.valid_position(i, j) and (0 <=  i != row or j != col):
                        self.dig(i, j)
        return True
    
    def remaining_available_positions(self):
        return self.num_rows * self.num_columns - (len(self.dug_positions) + self.num_bombs)

    def valid_position(self, i, j):
        return 0 <= i and i < self.num_rows and 0 <= j and j < self.num_columns