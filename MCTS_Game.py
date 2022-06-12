import numpy as np

class MCTS_Game:
    def __init__(self):
        self.newTileList = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]


    def init_game(self, board):
        board = np.zeros((4, 4), dtype=int)
        r = np.random.randint(0, 3)
        c = np.random.randint(0, 3)
        self.board[r][c] = 2
        return board

    def push_board(self, board):
        new_board = np.zeros((4, 4), dtype=int)
        done = False
        for row in range(4):
            count = 3
            for col in range(3, -1, -1):
                if board[row][col] != 0:
                    new_board[row][count] = board[row][col]
                    if col != count:
                        done = True
                    count -= 1

        return new_board, done

    def merge_board(self, board):
        score = 0
        done = False
        for row in range(4):
            for col in range(3, 0, -1):
                if board[row][col] == board[row][col-1] and board[row][col] != 0:
                    board[row][col] *= 2
                    score += board[row][col]
                    board[row][col-1] = 0
                    done = True
        
        return board, done, score

    def move_up(self, board):
        board = np.rot90(board, -1)
        board, has_pushed = self.push_board(board)
        board, has_merged, score = self.merge_board(board)
        board, _ = self.push_board(board)
        board = np.rot90(board)
        move_made = has_pushed or has_merged
        return board, move_made, score
    
    def move_down(self, board):
        board = np.rot90(board)
        board, has_pushed = self.push_board(board)
        board, has_merged, score = self.merge_board(board)
        board, _ = self.push_board(board)
        board = np.rot90(board, -1)
        move_made = has_pushed or has_merged
        return board, move_made, score

    def move_left(self, board):
        board = np.rot90(board, 2)
        board, has_pushed = self.push_board(board)
        board, has_merged, score = self.merge_board(board)
        board, _ = self.push_board(board)
        board = np.rot90(board, -2)
        move_made = has_pushed or has_merged
        return board, move_made, score

    def move_right(self, board):
        board, has_pushed = self.push_board(board)
        board, has_merged, score = self.merge_board(board)
        board, _ = self.push_board(board)
        move_made = has_pushed or has_merged
        return board, move_made, score

    def random_move(self, board):
        move_made = False
        moves = [self.move_up, self.move_down, self.move_left, self.move_right]
        while not move_made and(len(moves) > 0):
            move_index = np.random.randint(0, len(moves))
            move = moves[move_index]
            board, move_made, score = move(board)
            if move_made:
                return board, True, score
            moves.pop(move_index)
        return board, False, move
    
    def add_new_tile(self, board):
        tile_value = self.newTileList[np.random.randint(0, len(self.newTileList))]
        tile_row, tile_col = np.nonzero(np.logical_not(board))
        tile_loc = np.random.randint(0, len(tile_row))
        board[tile_row[tile_loc], tile_col[tile_loc]] = tile_value
        return board

    def check_win(board):
        return 2048 in board