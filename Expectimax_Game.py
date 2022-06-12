import numpy as np

class Expectimax_Game:
    def __init__(self):
        self.board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

    def move_line(self, cell):
        target = 0
        for i in range(1, 4):
            target_value = cell[target]
            current_value = cell[i]
            if current_value != 0:
                if target_value == 0:
                    cell[target] = current_value
                    cell[i] = 0
                else:
                    if target_value == current_value:
                        cell[i] = 0
                        cell[target] *= 2
                    else:
                        cell[i] = 0
                        cell[target + 1] = current_value
                    target += 1
        return 

    def move_up(self, board):
        for c in range(4):
            cell = []
            for r in range(4):
                cell.append(board[r][c])
            self.move_line(cell)
            for r in range(4):
                board[r][c] = cell[r]
        return 

    def move_down(self, board):
        for c in range(4):
            cell = []
            for r in range(4):
                cell.append(board[3-r][c])
            self.move_line(cell)
            for r in range(4):
                board[3-r][c] = cell[r]
        return 

    def move_left(self, board):
        for r in range(4):
            cell = []
            for c in range(4):
                cell.append(board[r][c])
            self.move_line(cell)
            for c in range(4):
                board[r][c] = cell[c]
        return 

    def move_right(self, board):
        for r in range(4):
            cell = []
            for c in range(4):
                cell.append(board[r][3-c])
            self.move_line(cell)
            for c in range(4):
                board[r][3-c] = cell[c]
        return
        
    def move(self, board, action):
        if action == 0:
            self.move_up(board)
        elif action == 1:
            self.move_down(board)
        elif action == 2:
            self.move_left(board)
        elif action == 3:
            self.move_right(board)
        
    def print_board(self):
        new_board = np.array(self.board)
        print(new_board)

    