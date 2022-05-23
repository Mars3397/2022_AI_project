from game import game
import expectimax

newGame = game()

board = [   [0, 0, 2, 0], 
            [4, 2, 0, 0], 
            [4, 4, 0, 0], 
            [8, 8, 0, 0]    ]

# newGame.printBoard(board)
# print("--------")
action = expectimax.getAction(newGame, board)
if action == 0:
    print("上")
elif action == 1:
    print("下")
elif action == 2:
    print("左")
elif action == 3:
    print("右")


