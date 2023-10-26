"""
Nine Men's Morris Player
"""

from copy import deepcopy
import numpy as np
import random

BEGINNER = "beginner"
INTERMEDIATE = "intermediate"

EMPTY = None
USER = 1
AI = 2


def initial_state():
    """
    Returns starting state of the board
    """

    return  [[EMPTY, "$", "$", EMPTY, "$", "$", EMPTY],
            ["$", EMPTY, "$", EMPTY, "$", EMPTY, "$"],
            ["$", "$", EMPTY, EMPTY, EMPTY, "$", "$"],
            [EMPTY, EMPTY, EMPTY, "$", EMPTY, EMPTY, EMPTY],
            ["$", "$", EMPTY, EMPTY, EMPTY, "$", "$"],
            ["$", EMPTY, "$", EMPTY, "$", EMPTY, "$"],
            [EMPTY, "$", "$", EMPTY, "$", "$", EMPTY]
            ]


def actions(board, difficulty):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # initialize a set of all possible moves
    moves = set()



def board_positions(board):
    """
    Returns a dictionary of the form {intersection: (index, value)}
    """
    # get the elements in each position of the board
    positions = []
    for index, cell in np.ndenumerate(np.array(board)):
        if cell != "$":
            positions.append([index, cell])
    
    # pair the positions to the intersection points
    return {i+1: position for i, position in enumerate(positions)}
            

def result(board, action, player):
    """
    Returns the board that results from making a move on the current board.
    And
    The next player after the move is made
    """
    newBoard = deepcopy(board)

    i, j = action

    if newBoard[i][j] != EMPTY:
        raise Exception("not a valid move")
    else:
        newBoard[i][j] = player
        new_player = 3 - player
    
    # return the new board state and the next player
    return newBoard, new_player


def winner(board):
    ...


def remaining_pieces(board):
    """
    Returns the number of user and ai pieces still left on the board
    """

    # set user and ai piece count
    user = 0
    ai = 0

    for row in board:
        for cell in row:
            if cell == USER: user += 1
            elif cell == AI: ai += 1

    return user, ai


def terminal(board, user_pieces, ai_pieces, r_user_pieces, r_ai_pieces):
    """
    Returns true is the game is over, False otherwise
    """
    
    # if either the player or the ai still has pieces left to place, game not over
    # phase 1
    if user_pieces > 0 or ai_pieces > 0:
        if r_user_pieces > 1 or r_ai_pieces > 1:
            return False
        else:
            return True
    
    else:
        p_1, p_2 = remaining_pieces(board)
        
        # if either player has only two pieces left then it's game over
        if p_1 < 3 or p_2 < 3:
            return True
    
    return False


def minimax(board, difficulty):
    """
    Returns the optimal action (i,j) for the AI.
    """
    # if difficulty == BEGINNER:
    #     # print([value[0] for value in board_positions(initial_state()).values()])
    #     choices = [value[0] for value in board_positions(board).values()]
    #     return random.choice(choices)


def main():
    board = initial_state()
    # minimax(initial_state(), BEGINNER)
    # print(minimax(initial_state(), BEGINNER))


if __name__ == "__main__":
    main()