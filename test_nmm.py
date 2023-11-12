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


def test_board_pieces():
    """
    Tests for the positions of all played pieces on the game board
    """
    board = nmm.initial_state()

    board = nmm.result(board, (0, 0), USER)
    assert nmm.board_pieces(board) == ({1: [(0, 0), USER]},
                                       {})

    board = nmm.result(board, (6, 6), AI)
    assert nmm.board_pieces(board) == ({1: [(0, 0), USER]},
                                       {24: [(6, 6), AI]})


def test_remove():
    """
    Tests for removing a piece from the game board
    """
    board = nmm.initial_state()
    board = nmm.result(board, (0, 0), USER)
    assert nmm.remove(board, (0, 0), AI) == nmm.initial_state()

    board = nmm.initial_state()
    board = nmm.result(board, (6, 6), AI)
    assert nmm.remove(board, (6, 6), USER) == nmm.initial_state()


def test_remove_valid():
    """
    Tests for valid removal of a piece from the game board
    """
    board = nmm.initial_state()
    board = nmm.result(board, (0, 0), USER)

    with pytest.raises(Exception):
        nmm.remove(board, (0, 0), USER)

    with pytest.raises(Exception):
        nmm.remove(board, (6, 6), AI)


def test_result():
    """
    Tests for updating the state of the game after playing a move
    """
    board = nmm.initial_state()
    assert nmm.result(board, (0, 0), USER) == [[USER, "$", "$", EMPTY, "$", "$", EMPTY],
                                               ["$", EMPTY, "$", EMPTY, "$", EMPTY, "$"],
                                               ["$", "$", EMPTY, EMPTY, EMPTY, "$", "$"],
                                               [EMPTY, EMPTY, EMPTY, "$", EMPTY, EMPTY, EMPTY],
                                               ["$", "$", EMPTY, EMPTY, EMPTY, "$", "$"],
                                               ["$", EMPTY, "$", EMPTY, "$", EMPTY, "$"],
                                               [EMPTY, "$", "$", EMPTY, "$", "$", EMPTY]]

    assert nmm.result(board, (6, 6), AI) == [[EMPTY, "$", "$", EMPTY, "$", "$", EMPTY],
                                             ["$", EMPTY, "$", EMPTY, "$", EMPTY, "$"],
                                             ["$", "$", EMPTY, EMPTY, EMPTY, "$", "$"],
                                             [EMPTY, EMPTY, EMPTY, "$", EMPTY, EMPTY, EMPTY],
                                             ["$", "$", EMPTY, EMPTY, EMPTY, "$", "$"],
                                             ["$", EMPTY, "$", EMPTY, "$", EMPTY, "$"],
                                             [EMPTY, "$", "$", EMPTY, "$", "$", AI]]


def test_result_valid():
    """
    Tests for valid updations of the game after playing a move
    """
    board = nmm.initial_state()
    board = nmm.result(board, (0, 0), USER)

    with pytest.raises(Exception):
        nmm.result(board, (0, 0), AI)

    with pytest.raises(Exception):
        nmm.result(board, (0, 0), USER)


def test_winner():
    """
    Tests for checking if there is a winner in the current state of the game
    """
    board = nmm.initial_state()

    assert not nmm.winner(board, 9, 9, 0, 0)

    assert not nmm.winner(board, 0, 0, 3, 3)

    assert nmm.winner(board, 0, 0, 2, 3) == AI

    assert nmm.winner(board, 0, 0, 3, 2) == USER


def test_check_double():
    """
    Tests for checking if two consecutive moves are made by the same player
    """
    board = nmm.initial_state()
    board = nmm.result(board, (0, 0), USER)
    board = nmm.result(board, (6, 6), AI)

    assert nmm.check_double(board, (0, 3), USER)
    assert nmm.check_double(board, (0, 6), USER)
    assert nmm.check_double(board, (3, 0), USER)
    assert nmm.check_double(board, (6, 0), USER)

    assert nmm.check_double(board, (6, 0), AI)
    assert nmm.check_double(board, (6, 3), AI)
    assert nmm.check_double(board, (0, 6), AI)
    assert nmm.check_double(board, (3, 6), AI)


def test_terminal():
    """
    Tests for checking if the game has reached its end or not
    """
    board = nmm.initial_state()

    assert nmm.terminal(board, 0, 1, 9, 8) == False

    assert nmm.terminal(board, 1, 0, 8, 9) == False

    assert nmm.terminal(board, 0, 0, 3, 3) == False

    assert nmm.terminal(board, 0, 0, 3, 2) == True

    assert nmm.terminal(board, 0, 0, 2, 3) == True

    assert nmm.terminal(board, 2, 2, 0, 0) == True

    assert nmm.terminal(board, 3, 3, 0, 0) == False
