import numpy as np
from Expectimax_Game import Expectimax_Game
from copy import deepcopy

class Expectimax:
    def __init__(self):
        self.weight = [
            [0.135759, 0.121925, 0.102812, 0.099937],
            [0.0997992, 0.0888405,  0.076711, 0.0724143],
            [0.060654, 0.0562579, 0.037116, 0.0161889],
            [0.0125498, 0.00992495, 0.00575871, 0.00335193]
        ]
        self.agent = Expectimax_Game()
        self.newTileList = [2, 4]
        self.newTileProb = [0.9, 0.1]

    def print_weight(self):
        print(np.array(self.weight))

    def compute_terminal_score(self, board):
        score0, score1, score2, score3 = 0, 0, 0, 0
        tscore0, tscore1, tscore2, tscore3 = 0, 0, 0, 0
        for r in range(4):
            for c in range(4):
                score0 += board[r][c] * self.weight[r][c]
                score1 += board[r][c] * self.weight[3 - c][r]
                score2 += board[r][c] * self.weight[3 - r][3 - c]
                score3 += board[r][c] * self.weight[c][3 - r]

                tscore0 += board[r][c] * self.weight[c][r]
                tscore1 += board[r][c] * self.weight[r][3 - c]
                tscore2 += board[r][c] * self.weight[3 - c][3 - r]
                tscore3 += board[r][c] * self.weight[3 - r][c]

        return max(score0, score1, score2, score3, tscore0, tscore1, tscore2, tscore3)


    def compute_score(self, board, depth):
        if depth == 0:
            return self.compute_terminal_score(board)
        else:
            totalScore = 0
            totalProb = 0
            for r in range(4):
                for c in range(4):
                    if board[r][c] == 0:
                        for i in range(2):
                            next_board = deepcopy(board)
                            next_board[r][c] = self.newTileList[i]
                            bestScore = 0
                            bestDirection = -1
                            for d in range(4):
                                next_board_moved = deepcopy(next_board)
                                self.agent.move(next_board_moved, d)
                                
                                if next_board_moved != next_board:
                                    score = self.compute_score(next_board_moved, depth-1)
                                    if score > bestScore:
                                        bestScore = score
                                        bestDirection = d
                                else:
                                    break
                            if bestDirection != -1:
                                totalScore += self.newTileProb[i] * bestScore
                            else:
                                totalScore += self.newTileProb[i] * self.compute_terminal_score(next_board)       
                            totalProb += self.newTileProb[i]
            return totalScore / totalProb

    def get_next_action(self, board, depth):
        bestScore = 0
        bestDirection = -1
        for d in range(4):
            moved = deepcopy(board)
            
            self.agent.move(moved, d)
            if moved != board:
                score = self.compute_score(moved, depth)
                if score > bestScore:
                    bestScore = score
                    bestDirection = d
            else:
                score = 0
        print(bestDirection)
        return bestDirection
