# -*- coding: utf-8 -*-
from dojo.task2 import PlayGround

TEXT = """4
4
0010
1010
0100
1111
4
1001
0000
0110
1001
5
10011
00100
00000
11111
00000
8
00100100
10000001
00100101
01000100
10000000
00110110
10110110
00000000
"""


def test_playground_read_input():
    playground = PlayGround(text=TEXT)
    assert len(playground.fields) == 4


def test_playground_get_solution():
    playground = PlayGround(text=TEXT)
    assert playground.get_solution() == [1, 3, 3, 9]


def test_field_setup_cells():
    expected = [
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (1, 1), (2, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3), (1, 3), (2, 3), (3, 3),
    ]

    playground = PlayGround(text=TEXT)
    field = playground.fields[0]
    field.setup_cells()
    assert field.todo == expected


def test_field_get_neighbours_of_this_cell():
    playground = PlayGround(text=TEXT)
    field = playground.fields[0]

    expected = [(0, 1), (0, 2), (0, 3), (1, 1), (1, 3), (2, 1), (2, 2), (2, 3)]
    assert expected == sorted(field.get_neighbours_of_cell(1, 2))

    expected = [(0, 1), (1, 0), (1, 1)]
    assert expected == sorted(field.get_neighbours_of_cell(0, 0))

    expected = [(2, 0), (2, 1), (3, 1)]
    assert expected == sorted(field.get_neighbours_of_cell(3, 0))

    expected = [(0, 1), (0, 3), (1, 1), (1, 2), (1, 3)]
    assert expected == sorted(field.get_neighbours_of_cell(0, 2))

    expected = [(0, 2), (1, 2), (1, 3)]
    assert expected == sorted(field.get_neighbours_of_cell(0, 3))

    expected = [(2, 1), (2, 2), (2, 3), (3, 1), (3, 3)]
    assert expected == sorted(field.get_neighbours_of_cell(3, 2))

    expected = [(2, 2), (2, 3), (3, 2)]
    assert expected == sorted(field.get_neighbours_of_cell(3, 3))


def test_field_get_solution():
    playground = PlayGround(text=TEXT)
    field = playground.fields[0]
    assert field.get_solution() == 1
