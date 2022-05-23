import random

from game import game

gameDepth = 2

def _expectimax(currentDepth, gameState, board, action, possibility):
    # return the evaluation value when reach the end state or the deepest depth
    if gameState.isLose(board) or currentDepth > gameDepth:
        evaluateBoard = [ row[:] for row in board ]
        return evaluationFunction(gameState, evaluateBoard, action, possibility)

    # store the following action scores of each actions 
    # -> apply max or min according to the agent of the level
    actionScores = []
    # get and store legal actions
    legalActions = gameState.getLegalActions(board)

    for a in legalActions:
        # extend the actions to the next state
        possibleStates = gameState.getPossibleStates(board, a)
        each = []
        for possibleState in possibleStates:
            nextState = [ row[:] for row in possibleState[0] ]
            each.append(_expectimax(currentDepth + 1, gameState, nextState, a, possibleState[1]))
        actionScores.append(max(each))
        # nextBoard = gameState.generateNextState(board, action)
        # actionScores.append(expectimax(currentDepth + 1, gameState, nextBoard))


    # return max action score
    if currentDepth == 1:
        return actionScores
    else:
        return max(actionScores)
        # return float(sum(actionScores) / len(actionScores))

def expectimax(currentDepth, gameState, board, possibility):
    # return the evaluation value when reach the end state or the deepest depth
    # if gameState.isLose(board) or currentDepth > gameDepth:
    #     evaluateBoard = [ row[:] for row in board ]
    #     return evaluationFunction(gameState, evaluateBoard, action, possibility)

    # store the following action scores of each actions 
    # -> apply max or min according to the agent of the level
    actionScores = []
    # get and store legal actions
    legalActions = gameState.getLegalActions(board)

    for action in legalActions:
        # extend the actions to the next state
        possibleStates = gameState.getPossibleStates(board, action)
        each = []
        for possibleState in possibleStates:
            nextState = [ row[:] for row in possibleState[0] ]
            each.append(_expectimax(currentDepth + 1, gameState, nextState, action, possibleState[1]))
        actionScores.append(max(each))
        # nextBoard = gameState.generateNextState(board, action)
        # actionScores.append(expectimax(currentDepth + 1, gameState, nextBoard))


    # return max action score
    if currentDepth == 1:
        return actionScores
    else:
        return max(actionScores)
        # return float(sum(actionScores) / len(actionScores))
            
def getAction(gameState, board):
    # get the following legal actions
    legalActions = gameState.getLegalActions(board)
    print(legalActions)
    # expectimax (depth, gameState) -> perform expectimax Search
    # which return the scores of following actions
    actionScores = expectimax(1, gameState, board, 1)
    print(actionScores)

    # Pick randomly among the best action score
    maxActionScore = max(actionScores)
    bestIndices = [index for index in range(len(actionScores)) 
                    if actionScores[index] == maxActionScore]
    chosenIndex = random.choice(bestIndices)

    return legalActions[chosenIndex]

def evaluationFunction (gameState, board, action, possibility): 
    """
    bonus : 
        1. "empty squres"
        2. "having large values on the edge"
        3. "counted the number of potential merges"
        4. "having monotonic rows and columns"
    """

    """
    90% will generate 2, 10% will generate 4
    每一次移動產生的新數字，會在空格的空格隨機產生，所以就會有期望值
    """
    nextBoard = gameState.generateNextState(board, action)
    countEmpty = gameState.countEmpty(nextBoard) - gameState.countEmpty(board)
    countEdges = gameState.countEdges(nextBoard) - gameState.countEdges(board)
    countMerges = gameState.countMergeScore(board, action)
    countMonotonic = gameState.countMonotonic(nextBoard) - gameState.countMonotonic(board)

    evaluateValue = (countEmpty + countEdges + countMerges + countMonotonic)

    return evaluateValue