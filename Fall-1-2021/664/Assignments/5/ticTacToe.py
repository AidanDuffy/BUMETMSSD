import numpy as np

class GameState:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.gameBoard = np.zeros((3,3)) # 3 by 3 tic tac toe board.
        self.whosMove = 1 #starts with id 1

class AITicPlayer:

    def __init__(self, id, exp_rate = 0.4):
        self.playerId = id
        self.exp = exp_rate
        self.states = []
        self.states_value = {}
        self.learning_rate = 0.2


    def getBoard(self, gameBoard):
        return str(gameBoard.reshape(3*3))

