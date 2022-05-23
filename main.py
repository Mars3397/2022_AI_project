from game import game
import expectimax

newGame = game()

board = [   [1, 2, 2, 1], 
            [1, 1, 2, 0], 
            [2, 2, 2, 2], 
            [3, 2, 3, 2]    ]

newGame.printBoard(board)
print("--------")
action = expectimax.getAction(newGame, board)
print(action)

