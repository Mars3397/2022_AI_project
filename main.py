from game import game

newGame = game()


newGame.printBoard(newGame.board)
print("--------")
newGame.getNextState(1)
newGame.printBoard(newGame.board)
print("--------")

