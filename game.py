from numpy import size


class game: 
    def getLegalActions(self, board): 
        # get possible action for the current board
        legalActions = []
        f1, f2 = True, True
        # for col
        t = self.getTranspose(board)
        for i in range(4):
            col = [s for s in t[i] if s != 0]
            if len(col) == 4:
                f2 = False
                for j in range(3):
                    if col[j] == col[j + 1]:
                        f2 = True
                        break
            if not f2:
                break
        if f2:
            legalActions.append(0)
            legalActions.append(1)
        # for row
        for i in range(4):
            row = [s for s in board[i] if s != 0]
            if len(row) == 4:
                f1 = False
                for j in range(3):
                    if row[j] == row[j + 1]:
                        f1 = True
                        break
            if not f1:
                break
        if not f1:
            legalActions.append(2)
            legalActions.append(3)
        
        return legalActions
    
    """------------------------------------------------------------------"""

    def generateNextState(self, _board, action):
        # get the board after the given action
        # up, down, left, right -> 0, 1, 2, 3
        board = [ row[:] for row in _board ]
        if action == 0:
            t = self.getTranspose(board)
            for i in range(4):
                row = [s for s in t[i] if s != 0]
                # print(row, end="->")
                mergeRow = []
                j = 0
                f = True
                while j < len(row) - 1:
                    if f and row[j] == row[j + 1]:
                        mergeRow.append(row[j] * 2)
                        f = False
                    else:
                        if f:
                            mergeRow.append(row[j])
                        else:
                            f = True
                        if j == len(row) - 2:
                            mergeRow.append(row[j + 1])
                    j += 1
                if len(row) == 1:
                    mergeRow.insert(0, row[-1])
                # print(mergeRow, end="->")
                while len(mergeRow) < 4:
                    mergeRow.append(0)
                # print(mergeRow)
                t[i] = mergeRow
            board = self.getTranspose(t)
        elif action == 1:
            t = self.getTranspose(board)
            for i in range(4):
                row = [s for s in t[i] if s != 0]
                # print(row, end="->")
                mergeRow = []
                j = len(row) - 1
                f = True
                while j > 0:
                    if f and row[j] == row[j - 1]:
                        mergeRow.insert(0, row[j] * 2)
                        f = False
                    else:
                        if f:
                            mergeRow.insert(0, row[j])
                        else:
                            f = True
                        if j == 1:
                            mergeRow.insert(0, row[j - 1])
                    j -= 1
                if len(row) == 1:
                    mergeRow.insert(0, row[-1])
                # print(mergeRow, end="->")
                while len(mergeRow) < 4:
                    mergeRow.insert(0, 0)
                # print(mergeRow)
                t[i] = mergeRow
            board = self.getTranspose(t)
        elif action == 2:
            for i in range(4):
                row = [s for s in board[i] if s != 0]
                # print(row, end="->")
                mergeRow = []
                j = 0
                f = True
                while j < len(row) - 1:
                    if f and row[j] == row[j + 1]:
                        mergeRow.append(row[j] * 2)
                        f = False
                    else:
                        if f:
                            mergeRow.append(row[j])
                        else:
                            f = True
                        if j == len(row) - 2:
                            mergeRow.append(row[j + 1])
                    j += 1
                if len(row) == 1:
                    mergeRow.insert(0, row[-1])
                # print(mergeRow, end="->")
                while len(mergeRow) < 4:
                    mergeRow.append(0)
                # print(mergeRow)
                board[i] = mergeRow
        else:
            for i in range(4):
                row = [s for s in board[i] if s != 0]
                # print(row, end="->")
                mergeRow = []
                j = len(row) - 1
                f = True
                while j > 0:
                    if f and row[j] == row[j - 1]:
                        mergeRow.insert(0, row[j] * 2)
                        f = False
                    else:
                        if f:
                            mergeRow.insert(0, row[j])
                        else:
                            f = True
                        if j == 1:
                            mergeRow.insert(0, row[j - 1])
                    j -= 1
                if len(row) == 1:
                    mergeRow.insert(0, row[-1])
                # print(mergeRow, end="->")
                while len(mergeRow) < 4:
                    mergeRow.insert(0, 0)
                # print(mergeRow)
                board[i] = mergeRow
        
        return board

    """------------------------------------------------------------------"""

    def getScore(self, board):
        # count the score of current board
        score = 0
        for i in range(4):
            for j in range(4):
                score += board[i][j]
        return score

    """------------------------------------------------------------------"""

    def countEmpty(self, board):
        # count how many squares are empty
        count = 0
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    count += 1
        return count

    """------------------------------------------------------------------"""

    def countEdges(self, board):
        # count how many big number (>= 512) are on the edge
        count = 0
        for i in range(4):
            for j in range(4):
                if board[i][j] >= 512:
                    if i == 0 or i == 4 or j == 0 or j == 4:
                        count += 1
        return count

    """------------------------------------------------------------------"""

    def countMerges(self, board):
        # count there are how many potential merge
        count = 0
        origin = self.countEmpty(board)
        movedBoards = [ self.generateNextState(board, i) for i in range(4) ]

        for i in range(4):
            count += (self.countEmpty(movedBoards[i]) - origin)
        return count / 2

    """------------------------------------------------------------------"""

    def getTranspose(self, board):
        # get the tranpose of the board
        transpose = [[0, 0, 0, 0], 
                     [0, 0, 0, 0], 
                     [0, 0, 0, 0], 
                     [0, 0, 0, 0]]
        for i in range(4):
            for j in range(4):
                transpose[i][j] = board[j][i]
        return transpose

    """------------------------------------------------------------------"""
    
    def countMonotonic(self, board):
        # count how many rows and cols are monotonic
        count = 0
        # for rows
        for i in range(4):
            s1 = set()
            temp = [s for s in board[i] if s != 0]
            for j in range(len(temp) - 1):
                if temp[j] < temp[j + 1]:
                    s1.add(False)
                else:
                    s1.add(True)
            if len(s1) <= 1:
                count += 1

        # for cols
        t = self.getTranspose(board)
        for i in range(4):
            s2 = set()
            temp = [s for s in t[i] if s != 0]
            for j in range(len(temp) - 1):
                if temp[j] < temp[j + 1]:
                    s2.add(False)
                else:
                    s2.add(True)
            if len(s2) <= 1:
                count += 1
            
        return count

    """------------------------------------------------------------------"""

    def printBoard(self, board):
        # print out the given board
        for i in range(4):
            for j in range(4):
                print(board[i][j], end=" ")
            print()

    """------------------------------------------------------------------"""

    def getPossibleStates(self, board, action):
        # get possible states for the action
        possibleStates = []
        movedState = self.generateNextState(board, action)
        numEmpty = self.countEmpty(movedState)

        for i in range(4):
            for j in range(4):
                if movedState[i][j] == 0:
                    copyBoard = [row[:] for row in movedState]
                    copyBoard2 = [row[:] for row in movedState]
                    copyBoard[i][j] = 4
                    possibleStates.append([copyBoard, (1 / numEmpty) * 0.1])
                    copyBoard2[i][j] = 2
                    possibleStates.append([copyBoard2, (1 / numEmpty) * 0.9])

        return possibleStates

    """------------------------------------------------------------------"""

    def isLose(self, board):
        arr = self.getLegalActions(board)
        if len(arr) == 0:
            return True
        else:
            return False


