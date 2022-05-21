import random

gameDepth = 5

def expectimax(currentDepth, gameState):
    # return the evaluation value when reach the end state or the deepest depth
    if gameState.isLose() or currentDepth > gameDepth:
        return evaluationFunction(gameState)

    # store the following action scores of each actions 
    # -> apply max or min according to the agent of the level
    actionScores = []
    # get and store legal actions
    legalActions = gameState.getLegalActions()

    for action in legalActions:
        # extend the actions to the next state
        nextState = gameState.getNextState(action)
        actionScores.append(expectimax(currentDepth + 1, nextState))

    # return max action score
    if currentDepth == 1:
        return actionScores
    else:
        return max(actionScores)
        # return float(sum(actionScores) / len(actionScores))
            
def getAction(gameState):
    # get the following legal actions
    legalActions = gameState.getLegalActions(0)

    # expectimax (depth, gameState) -> perform expectimax Search
    # which return the scores of following actions
    actionScores = expectimax(1, gameState)

    # Pick randomly among the best action score
    maxActionScore = max(actionScores)
    bestIndices = [index for index in range(len(actionScores)) 
                    if actionScores[index] == maxActionScore]
    chosenIndex = random.choice(bestIndices)

    return legalActions[chosenIndex]

def evaluationFunction (gameState): 
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
    nextGameState = gameState.getNextState(action)
    currentScore = gameState.getScore(gameState)
    futureScore = gameState.getScore(nextGameState)
    bonus_1 = gameState.countEmpty(gameState)
    bonus_2 = gameState.countEdges(gameState)
    bouns_3 = gameState.countMerges(gameState)
    penalty_1 = gameState.countMonotonic(gameState)

    return gameState.countScore()