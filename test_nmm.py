import nmm
import pytest

EMPTY = nmm.EMPTY
USER = nmm.USER
AI = nmm.AI


def test_initial_state():
    assert nmm.initial_state() == [[EMPTY, "$", "$", EMPTY, "$", "$", EMPTY],
                                   ["$", EMPTY, "$", EMPTY, "$", EMPTY, "$"],
                                   ["$", "$", EMPTY, EMPTY, EMPTY, "$", "$"],
                                   [EMPTY, EMPTY, EMPTY, "$", EMPTY, EMPTY, EMPTY],
                                   ["$", "$", EMPTY, EMPTY, EMPTY, "$", "$"],
                                   ["$", EMPTY, "$", EMPTY, "$", EMPTY, "$"],
                                   [EMPTY, "$", "$", EMPTY, "$", "$", EMPTY]
                                   ]