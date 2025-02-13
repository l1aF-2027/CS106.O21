# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a currentGameState evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor currentGameStates
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the currentGameState, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        #return successorGameState.getScore()
        food = currentGameState.getFood()
        currentPos = list(successorGameState.getPacmanPosition())
        distance = float("-Inf")

        foodList = food.asList()

        if action == 'Stop':
            return float("-Inf")

        for currentGameState in newGhostStates:
            if currentGameState.getPosition() == tuple(currentPos) and (currentGameState.scaredTimer == 0):
                return float("-Inf")

        for x in foodList:
            tempDistance = -1 * (manhattanDistance(currentPos, x))
            if (tempDistance > distance):
                distance = tempDistance

        return distance


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the currentGameState.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        # return self.MiniMax(gameState, 0, 0)
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIdx):
        Returns a list of legal actions for an agent
        agentIdx=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIdx, action):
        Returns the successor game currentGameState after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game currentGameState is a winning currentGameState

        gameState.isLose():
        Returns whether or not the game currentGameState is a losing currentGameState
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        def minimax(currentGameState):
            bestValue, bestAction = None, None
            value = []
            for action in currentGameState.getLegalActions(0):
                #value = max(value,minValue(currentGameState.generateSuccessor(0, action), 1, 1))
                succ  = minValue(currentGameState.generateSuccessor(0, action), 1, 1)
                value.append(succ)
                if bestValue is None:
                    bestValue = succ
                    bestAction = action
                else:
                    if succ > bestValue:
                        bestValue = succ
                        bestAction = action
            return bestAction

        def minValue(currentGameState, agentIdx, depth):
            if agentIdx == currentGameState.getNumAgents():
                return maxValue(currentGameState, 0, depth + 1)
            value = None
            for action in currentGameState.getLegalActions(agentIdx):
                succ = minValue(currentGameState.generateSuccessor(agentIdx, action), agentIdx + 1, depth)
                if value is None:
                    value = succ
                else:
                    value = min(value, succ)

            if value is not None:
                return value
            else:
                return self.evaluationFunction(currentGameState)


        def maxValue(currentGameState, agentIdx, depth):
            if depth > self.depth:
                return self.evaluationFunction(currentGameState)
            value = None
            for action in currentGameState.getLegalActions(agentIdx):
                succ = minValue(currentGameState.generateSuccessor(agentIdx, action), agentIdx + 1, depth)
                if value is None:
                    value = succ
                else:
                    value = max(value, succ)
                
            if value is not None:
                return value
            else:
                return self.evaluationFunction(currentGameState)

        action = minimax(gameState)

        return action

        # def minimax_search(currentGameState, agentIdx, depth):
        #     # if in min layer and last ghost
        #     if agentIdx == currentGameState.getNumAgents():
        #         # if reached max depth, evaluate currentGameState
        #         if depth == self.depth:
        #             return self.evaluationFunction(currentGameState)
        #         # otherwise start new max layer with bigger depth
        #         else:
        #             return minimax_search(currentGameState, 0, depth + 1)
        #     # if not min layer and last ghost
        #     else:
        #         moves = currentGameState.getLegalActions(agentIdx)
        #         # if nothing can be done, evaluate the currentGameState
        #         if len(moves) == 0:
        #             return self.evaluationFunction(currentGameState)
        #         # get all the minimax values for the next layer with each node being a possible currentGameState after a move
        #         next = (minimax_search(currentGameState.generateSuccessor(agentIdx, m), agentIdx + 1, depth) for m in moves)

        #         # if max layer, return max of layer below
        #         if agentIdx == 0:
        #             return max(next)
        #         # if min layer, return min of layer below
        #         else:
        #             return min(next)
        # # select the action with the greatest minimax value
        # result = max(gameState.getLegalActions(0), key=lambda x: minimax_search(gameState.generateSuccessor(0, x), 1, 1))

        # return result        

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        
        def alphaBetaPruning(currentGameState):
            bestValue, bestAction = float("-inf"), None
            alpha = float("-inf")
            beta = float("inf")
            for action in currentGameState.getLegalActions(0):
                successor_currentGameState = currentGameState.generateSuccessor(0, action)
                value = minValue(successor_currentGameState, 1, 1, alpha, beta)
                if value > bestValue:
                    bestValue = value
                    bestAction = action
                    alpha = bestValue
            return bestAction

        def minValue(currentGameState, agentIdx, depth, alpha, beta):
            if agentIdx == currentGameState.getNumAgents():
                return maxValue(currentGameState, 0, depth + 1, alpha, beta)
            value = float("inf")
            for action in currentGameState.getLegalActions(agentIdx):
                succ = minValue(currentGameState.generateSuccessor(agentIdx, action), agentIdx + 1, depth, alpha, beta)
                value = min(value, succ)
                if value < alpha:
                    return value
                beta = min(value, beta)

            if value != float("inf"):
                return value
            else:
                return self.evaluationFunction(currentGameState)

        def maxValue(currentGameState, agentIdx, depth, alpha, beta):
            if depth > self.depth or currentGameState.isWin() or currentGameState.isLose():
                return self.evaluationFunction(currentGameState)
            value = float("-inf")
            for action in currentGameState.getLegalActions(agentIdx):
                succ = minValue(currentGameState.generateSuccessor(agentIdx, action), agentIdx + 1, depth, alpha, beta)
                value = max(value, succ)
                if value > beta :
                    return value
                alpha = max(alpha,value)    
            if value != float("-inf"):
                return value
            else:
                return self.evaluationFunction(currentGameState)

        action = alphaBetaPruning(gameState)
        return action

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expectimax(currentGameState):
            bestValue, bestAction = float("-inf"), None
            for action in currentGameState.getLegalActions(0):
                successor_currentGameState = currentGameState.generateSuccessor(0, action)
                value = expValue(successor_currentGameState, 1, 1)
                if value > bestValue:
                    bestValue = value
                    bestAction = action
                
            return bestAction

        def expValue(currentGameState, agentIdx, depth):
            if agentIdx == currentGameState.getNumAgents():
                return maxValue(currentGameState, 0, depth + 1)
            value = 0
            count_value = 0
            for action in currentGameState.getLegalActions(agentIdx):
                successor_currentGameState = currentGameState.generateSuccessor(agentIdx, action)
                value += expValue(successor_currentGameState, agentIdx + 1, depth)
                count_value += 1
            try:
                return value/ count_value
            except ZeroDivisionError:
                return self.evaluationFunction(currentGameState)

        def maxValue(currentGameState, agentIdx, depth):
            if depth > self.depth or currentGameState.isWin() or currentGameState.isLose():
                return self.evaluationFunction(currentGameState)
            bestValue = float("-inf")
            for action in currentGameState.getLegalActions(agentIdx):
                successor_currentGameState = currentGameState.generateSuccessor(agentIdx, action)
                value = expValue(successor_currentGameState, agentIdx + 1, depth)
                bestValue = max(value,bestValue)

            return bestValue
        action = expectimax(gameState)
        return action

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newCapsule = currentGameState.getCapsules()
    newGhostStates = currentGameState.getGhostStates()
    score = currentGameState.getScore()
    eatenWeight = 300
    ghostWeight = 20
    foodWeight = 10
    numWeight = 500
    
    update = 0
    ghostDistance =[manhattanDistance(newPos,ghost.getPosition()) for ghost in newGhostStates]
    for ghost in newGhostStates:
      if ghostDistance:
        if ghost.scaredTimer:
            ghostDistance_temp = manhattanDistance(newPos,ghost.getPosition()) 
            update += eatenWeight/float(ghostDistance_temp)
        else:
            if min(ghostDistance) == 0:
                update += -99999999
            else:
                update -= ghostWeight/float(min(ghostDistance))
            

    score = score + update
    foodDistance = [manhattanDistance(newPos,food) for food in newFood.asList()]
    foodOrCapsuleDistance = foodDistance + [manhattanDistance(newPos,capsule) for capsule in newCapsule]
    if foodOrCapsuleDistance:
        update = foodWeight/float(min(foodOrCapsuleDistance))
        score = score + update
    return score + numWeight/(len(newFood.asList())+1)


# Abbreviation
better = betterEvaluationFunction
