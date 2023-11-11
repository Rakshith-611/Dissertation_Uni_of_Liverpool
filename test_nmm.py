import nmm
import pytest

EMPTY = nmm.EMPTY
USER = nmm.USER
AI = nmm.AI


def test_initial_state():
    """
    Test for the initialization of the game board
    """
    assert nmm.initial_state() == [[EMPTY, "$", "$", EMPTY, "$", "$", EMPTY],
                                   ["$", EMPTY, "$", EMPTY, "$", EMPTY, "$"],
                                   ["$", "$", EMPTY, EMPTY, EMPTY, "$", "$"],
                                   [EMPTY, EMPTY, EMPTY, "$", EMPTY, EMPTY, EMPTY],
                                   ["$", "$", EMPTY, EMPTY, EMPTY, "$", "$"],
                                   ["$", EMPTY, "$", EMPTY, "$", EMPTY, "$"],
                                   [EMPTY, "$", "$", EMPTY, "$", "$", EMPTY]]


def test_board_positions_empty():
    """
    Tests the mapping for all playable positions
    """
    board = nmm.initial_state()
    assert nmm.board_positions(board) == {1: [(0, 0), EMPTY],
                                          2: [(0, 3), EMPTY],
                                          3: [(0, 6), EMPTY],
                                          4: [(1, 1), EMPTY],
                                          5: [(1, 3), EMPTY],
                                          6: [(1, 5), EMPTY],
                                          7: [(2, 2), EMPTY],
                                          8: [(2, 3), EMPTY],
                                          9: [(2, 4), EMPTY],
                                          10: [(3, 0), EMPTY],
                                          11: [(3, 1), EMPTY],
                                          12: [(3, 2), EMPTY],
                                          13: [(3, 4), EMPTY],
                                          14: [(3, 5), EMPTY],
                                          15: [(3, 6), EMPTY],
                                          16: [(4, 2), EMPTY],
                                          17: [(4, 3), EMPTY],
                                          18: [(4, 4), EMPTY],
                                          19: [(5, 1), EMPTY],
                                          20: [(5, 3), EMPTY],
                                          21: [(5, 5), EMPTY],
                                          22: [(6, 0), EMPTY],
                                          23: [(6, 3), EMPTY],
                                          24: [(6, 6), EMPTY]}


def test_board_positions_played():
    """
    Tests the mapping for a single round of play
    """
    board = nmm.initial_state()

    board = nmm.result(board, (0, 0), USER)
    assert nmm.board_positions(board) == {1: [(0, 0), USER],
                                          2: [(0, 3), EMPTY],
                                          3: [(0, 6), EMPTY],
                                          4: [(1, 1), EMPTY],
                                          5: [(1, 3), EMPTY],
                                          6: [(1, 5), EMPTY],
                                          7: [(2, 2), EMPTY],
                                          8: [(2, 3), EMPTY],
                                          9: [(2, 4), EMPTY],
                                          10: [(3, 0), EMPTY],
                                          11: [(3, 1), EMPTY],
                                          12: [(3, 2), EMPTY],
                                          13: [(3, 4), EMPTY],
                                          14: [(3, 5), EMPTY],
                                          15: [(3, 6), EMPTY],
                                          16: [(4, 2), EMPTY],
                                          17: [(4, 3), EMPTY],
                                          18: [(4, 4), EMPTY],
                                          19: [(5, 1), EMPTY],
                                          20: [(5, 3), EMPTY],
                                          21: [(5, 5), EMPTY],
                                          22: [(6, 0), EMPTY],
                                          23: [(6, 3), EMPTY],
                                          24: [(6, 6), EMPTY]}

    board = nmm.result(board, (6, 6), AI)
    assert nmm.board_positions(board) == {1: [(0, 0), USER],
                                          2: [(0, 3), EMPTY],
                                          3: [(0, 6), EMPTY],
                                          4: [(1, 1), EMPTY],
                                          5: [(1, 3), EMPTY],
                                          6: [(1, 5), EMPTY],
                                          7: [(2, 2), EMPTY],
                                          8: [(2, 3), EMPTY],
                                          9: [(2, 4), EMPTY],
                                          10: [(3, 0), EMPTY],
                                          11: [(3, 1), EMPTY],
                                          12: [(3, 2), EMPTY],
                                          13: [(3, 4), EMPTY],
                                          14: [(3, 5), EMPTY],
                                          15: [(3, 6), EMPTY],
                                          16: [(4, 2), EMPTY],
                                          17: [(4, 3), EMPTY],
                                          18: [(4, 4), EMPTY],
                                          19: [(5, 1), EMPTY],
                                          20: [(5, 3), EMPTY],
                                          21: [(5, 5), EMPTY],
                                          22: [(6, 0), EMPTY],
                                          23: [(6, 3), EMPTY],
                                          24: [(6, 6), AI]}
    

def test_actions():
    """
    Tests for all available actions on the board for a player
    """
    board = nmm.initial_state()
    assert nmm.actions(board, USER, 9, 9) == [(0, 0), (0, 3), (0, 6),
                                              (1, 1), (1, 3), (1, 5),
                                              (2, 2), (2, 3), (2, 4),
                                              (3, 0), (3, 1), (3, 2),
                                              (3, 4), (3, 5), (3, 6),
                                              (4, 2), (4, 3), (4, 4),
                                              (5, 1), (5, 3), (5, 5),
                                              (6, 0), (6, 3), (6, 6)]
    
    board = nmm.result(board, (0, 0), USER)
    assert nmm.actions(board, AI, 8, 9) == [(0, 3), (0, 6),
                                            (1, 1), (1, 3), (1, 5),
                                            (2, 2), (2, 3), (2, 4),
                                            (3, 0), (3, 1), (3, 2),
                                            (3, 4), (3, 5), (3, 6),
                                            (4, 2), (4, 3), (4, 4),
                                            (5, 1), (5, 3), (5, 5),
                                            (6, 0), (6, 3), (6, 6)]
    
    board = nmm.result(board, (6, 6), AI)
    assert nmm.actions(board, USER, 8, 8) == [(0, 3), (0, 6),
                                              (1, 1), (1, 3), (1, 5),
                                              (2, 2), (2, 3), (2, 4),
                                              (3, 0), (3, 1), (3, 2),
                                              (3, 4), (3, 5), (3, 6),
                                              (4, 2), (4, 3), (4, 4),
                                              (5, 1), (5, 3), (5, 5),
                                              (6, 0), (6, 3)]


board = nmm.initial_state()
print(nmm.actions(board, USER, 9, 9))

