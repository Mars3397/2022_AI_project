import numpy as np
from MCTS_Game import MCTS_Game
from copy import deepcopy


class MonteCarloTreeSearch:
    def __init__(self):
        self.agent = MCTS_Game()
        

    def get_next_action(self, board, search_per_move, search_length):
        moves = [self.agent.move_up, self.agent.move_down, self.agent.move_left, self.agent.move_right]
        scores = [0, 0, 0, 0]
        for i in range(4):
            first_move = moves[i]
            first_board, first_move_made, first_score = first_move(board)
            if first_move_made:
                first_board = self.agent.add_new_tile(first_board)
                scores[i] += first_score
            else:
                continue
            
            for _ in range(search_per_move):
                move_number = 1
                search_board = np.copy(first_board)
                game_valid = True
                while game_valid and move_number < search_length:
                    search_board, game_valid, search_score = self.agent.random_move(search_board)
                    if game_valid:
                        search_board = self.agent.add_new_tile(search_board)
                        scores[i] += search_score
                        move_number += 1
        best_action = np.argmax(scores)
        return best_action