# -*- coding: utf-8 -*-
from dojo.task2 import PlayGround

TEXTA = """4
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

TEXT = """3
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
"""


def test_playground_read_input():
    playground = PlayGround(text=TEXT)
    assert len(playground.fields) == 3
    assert playground.number_of_fields == 3


def test_playground_get_solution():
    playground = PlayGround(text=TEXT)
    playground.get_solution()


def test_field_get_all_cells():
    expected = [
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (1, 1), (2, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3), (1, 3), (2, 3), (3, 3),
    ]

    playground = PlayGround(text=TEXT)
    field = playground.fields[0]
    field.get_all_cells()
    assert field.todo == expected


def test_get_neighbours_of_this_cell():
    playground = PlayGround(text=TEXT)
    field = playground.fields[0]

    cell = (1, 2)
    expected = [(0, 1), (0, 2), (0, 3), (1, 1), (1, 3), (2, 1), (2, 2), (2, 3)]
    assert expected == sorted(field.get_neighbours_of_cell(cell))

    cell = (0, 0)
    expected = [(0, 1), (1, 0), (1, 1)]
    assert expected == sorted(field.get_neighbours_of_cell(cell))

    cell = (3, 0)
    expected = [(2, 0), (2, 1), (3, 1)]
    assert expected == sorted(field.get_neighbours_of_cell(cell))

    cell = (0, 2)
    expected = [(0, 1), (0, 3), (1, 1), (1, 2), (1, 3)]
    assert expected == sorted(field.get_neighbours_of_cell(cell))

    cell = (0, 3)
    expected = [(0, 2), (1, 2), (1, 3)]
    assert expected == sorted(field.get_neighbours_of_cell(cell))

    cell = (3, 2)
    expected = [(2, 1), (2, 2), (2, 3), (3, 1), (3, 3)]
    assert expected == sorted(field.get_neighbours_of_cell(cell))

    cell = (3, 3)
    expected = [(2, 2), (2, 3), (3, 2)]
    assert expected == sorted(field.get_neighbours_of_cell(cell))
