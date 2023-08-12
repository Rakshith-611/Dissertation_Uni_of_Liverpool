"""
Nine Men's Morris Player
"""

from copy import deepcopy


def initial_state():
    """
    Returns starting state of the board
    """

    return [[None, "$", "$", None, "$", "$", None],
            ["$", None, "$", None, "$", None, "$"],
            ["$", "$", None, None, None, "$", "$"],
            [None, None, None, "$", None, None, None],
            ["$", "$", None, None, None, "$", "$"],
            ["$", None, "$", None, "$", None, "$"],
            [None, "$", "$", None, "$", "$", None]
            ]