"""
Nine Men's Morris Player
"""

from copy import deepcopy
import numpy as np
import random
from collections import Counter
import math

BEGINNER = 'beginner'
INTERMEDIATE = 'intermediate'
HARD = 'hard'

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


def actions(board, player, user_pieces, ai_pieces):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    if player == USER and user_pieces > 0:
        positions = board_positions(board)
        return [positions[position][0] for position in positions if positions[position][1] == EMPTY]
    if player == AI and ai_pieces > 0:
        positions = board_positions(board)
        return [positions[position][0] for position in positions if positions[position][1] == EMPTY]


def board_pieces(board):
    """
    Returns the pieces and the positions of player and ai
    """
    positions = board_positions(board)
    
    user_pieces = {}
    ai_pieces = {}
    for position in positions:
        if positions[position][1] == USER:
            user_pieces[position] = positions[position]
        elif positions[position][1] == AI:
            ai_pieces[position] = positions[position]
    
    return user_pieces, ai_pieces


def remove(board, action, player):
    """
    Removes an opponent piece
    """
    newBoard = deepcopy(board)

    i, j = action

    if newBoard[i][j] == EMPTY or newBoard[i][j] == player:
        raise Exception("not a valid move")
    else:
        newBoard[i][j] = EMPTY

    return newBoard
            

def result(board, action, player):
    """
    Returns the board that results from making a move on the current board.
    """
    newBoard = deepcopy(board)

    i, j = action

    if newBoard[i][j] != EMPTY:
        raise Exception("not a valid move")
    else:
        newBoard[i][j] = player
    
    # return the new board state and the next player
    return newBoard


def winner(board, user_pieces, ai_pieces, r_user_pieces, r_ai_pieces):
    """
    Returns the winner of the game, if there is one.
    """
    # can't have a winner until total remaining pieces is still 3 or more
    if user_pieces > 0 or ai_pieces > 0:
        if ((user_pieces + r_user_pieces) > 2) or ((ai_pieces + r_ai_pieces) > 3):
            return None
    
    else:
        if r_user_pieces < 3: return AI
        elif r_ai_pieces < 3: return USER


def check_double(board, action, player):
    """
    Returns true if there are 2 in a line of any player pieces
    """
    newBoard = deepcopy(board)
    newBoard = result(newBoard, action, player)
    arr = np.array(newBoard)
    row, col = arr[action[0]], arr[:, action[1]]

    lines = [row, col]

    if row[3] == "$":
        lines.pop(0)
        row_a, row_b = row[:3], row[4:]
        if action[0] < 3:
            lines.append(row_b)
        else:
            lines.append(row_a)
    if col[3] == "$":
        lines.pop(-1)
        column_a, column_b = col[:3], col[4:]
        if action[1] < 3:
            lines.append(column_b)
        else:
            lines.append(column_a)

    lines = [np.ndarray.tolist(line) for line in lines]
    for line in lines:
        if "$" in line:
            while "$" in line:
                line.remove("$")

    for line in lines:
        if line.count(player) == 2:
            return True


def check_triple(board, action, player):
    """
    Returns true if there is a 3 in a row of any player pieces
    """
    newBoard = deepcopy(board)
    newBoard = result(newBoard, action, player)
    arr = np.array(newBoard)
    # get the row and column where the move was made
    row, column = arr[action[0]], arr[:, action[1]]

    lines = [row, column]
    # edge case for middle row or column
    if row[3] == "$":
        lines.pop(0)
        row_a, row_b = row[:3], row[4:]
        if action[0] < 3:
            lines.append(row_b)
        else:
            lines.append(row_a)
    if column[3] == "$":
        lines.pop(-1)
        column_a, column_b = column[:3], column[4:]
        if action[1] < 3:
            lines.append(column_b)
        else:
            lines.append(column_a)

    # Check if all elements in each line (except '$') are equal to 'player'
    for line in lines:
        if np.all(line[line != "$"] == player):
            return True

    return False


def terminal(board, user_pieces, ai_pieces, r_user_pieces, r_ai_pieces):
    """
    Returns true is the game is over, False otherwise
    """
    
    # if either the player or the ai still has pieces left to place, game not over
    if user_pieces > 0 or ai_pieces > 0:
        if ((user_pieces+r_user_pieces) < 3) or ((ai_pieces+r_ai_pieces) < 3):
            return True
        else:
            return False
    
    else:
        p_1, p_2 = r_user_pieces, r_ai_pieces
        
        # if either player has only two pieces left then it's game over
        if p_1 < 3 or p_2 < 3:
            return True
    
    return False


def utility(board, action, player):
    """
    Returns the utility value of the board
    """
    if player == USER:
        if check_triple(board, action, player):
            return 1
        elif check_double(board, action, player):
            return 0.5
        else:
            return 0
    elif player == AI:
        if check_triple(board, action, player):
            return -1
        elif check_double(board, action, player):
            return -0.5
        else:
            return 0


def minimax(board, difficulty, player, user_pieces, ai_pieces):
    """
    Returns the optimal action (i,j) for the AI.
    """
    # beginner difficulty, make a random move
    if difficulty == BEGINNER:
        return random.choice(actions(board, player, user_pieces, ai_pieces))
    
    # intermediate difficulty, make only the next best move
    elif difficulty == INTERMEDIATE:
        moves = []
        v = math.inf

        for move in actions(board, player, user_pieces, ai_pieces):
            if utility(board, move, player) <= v:
                v = utility(board, move, player)
        
        for move in actions(board, player, user_pieces, ai_pieces):
            if utility(board, move, player) == v:
                moves.append((move, v))

        best_action = random.choice([x[0] for x in moves])
        return best_action
    
    # hard difficulty, make a move looking 2 turns forward
    elif difficulty == HARD:
        ...


def main():
    board = initial_state()
    
    board = result(board, (0,0), USER)
    # print(actions(board, AI, 8, 9))
    board = result(board, (0,3), AI)

    board = result(board, (3,0), USER)
    # check_double(board, (1, 3), 2)
    # board = result(board, (1,3), AI)

    # print(utility(board, (6,0), 1))

    # board = result(board, (6,0), USER)
    # board = result(board, (2,3), AI)
    # max_value(board, 1, (6,6), USER, 7, 7)
    print(minimax(board, INTERMEDIATE, AI, 7, 8))


if __name__ == "__main__":
    main()