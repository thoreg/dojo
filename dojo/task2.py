# -*- coding: utf-8 -*-
import logging
import re

log = logging.getLogger('werkzeug')

IS_ONE_DIGIT = re.compile(r'\d$')


class Field:
    """
    Square field of '0's and '1's.

    """
    def __init__(self, dimension, field_lines):
        self.dimension = int(dimension)
        self.content = field_lines
        self.todo = []

    def get_solution(self):
        self.get_all_cells()
        self.walk_through_all_cells()
        # self.debug()

    def walk_through_all_cells(self):
        to_check = set()
        print
        print "content: "
        print self.content

        self.todo = sorted(self.todo)
        print "todo: "
        print self.todo

        number_of_groups = 0

        seen = set()

        while self.todo:
            x, y = self.todo.pop()
            if (x, y) in seen:
                continue

            print "x: {}, y: {} : {}".format(x, y, self.content[y][x])

            if self.content[y][x] == '1':
                print
                print "New Cell to check found: ({}, {})".format(x, y)
                to_check.add((x, y))
                number_of_groups += 1

            while to_check:
                (x, y) = to_check.pop()
                if (x, y) in seen:
                    print "cell {} already seen".format((x, y))
                    continue

                neighbours = self.get_neighbours_of_cell((x, y))
                for nx, ny in neighbours:
                    if self.content[nx][ny] == '1':
                        to_check.add((nx, ny))

                    seen.add((nx, ny))
                    print "2check: {}".format(to_check)

            seen.add((x, y))

        print
        print "to_check: "
        print sorted(to_check)
        print "Number_of_units: {}".format(number_of_groups)
        print

    def get_all_cells(self):
        row = 0
        for index, digit in enumerate(range(self.dimension**2)):
            if not index == 0 and index % self.dimension == 0:
                row += 1

            self.todo.append((index % self.dimension, row))

    def get_neighbours_of_cell(self, cell):
        """
        ---------------
        | NW | N | NO |
        ---------------
        |  W | x |  O |
        ---------------
        | SW | S | SO |
        ---------------

        """
        x = cell[0]
        y = cell[1]
        neighbours = set()

        minimal_x = minimal_y = 0
        maximal_x = maximal_y = self.dimension - 1

        # N
        neighbours.add((x, max(y - 1, minimal_y)))

        # NO
        neighbours.add((min(x + 1, maximal_x), max(y - 1, minimal_y)))

        # O
        neighbours.add((min(x + 1, maximal_x), y))

        # SO
        neighbours.add((min(x + 1, maximal_x), min(y + 1, maximal_y)))

        # S
        neighbours.add((x, min(y + 1, maximal_y)))

        # SW
        neighbours.add((max(x - 1, minimal_x), min(y + 1, maximal_y)))

        # W
        neighbours.add((max(x - 1, minimal_x), y))

        # NW
        neighbours.add((max(x - 1, minimal_x), max(y - 1, minimal_y)))

        # A cell can not be the neighbour of itself
        if cell in neighbours:
            neighbours.remove(cell)

        return sorted(neighbours)


class PlayGround:
    """
    Class to find out how many units of '1's are available in a field of '0's and '1's.

    """
    def __init__(self, text=''):
        self.number_of_fields = 0
        self.fields = []
        for line_number, line in enumerate(text.splitlines()):
            if line_number == 0:
                self.number_of_fields = int(line)
                continue

            # A new field begins
            if IS_ONE_DIGIT.match(line):
                dimension = int(line)
                field_lines = []
                lines_left = dimension
                continue

            if lines_left:
                field_lines.append(line)
                lines_left -= 1
                if lines_left == 0:
                    self.fields.append(Field(dimension, field_lines))

    def get_solution(self):
        solutions = []
        for field in self.fields:
            solutions.append(field.get_solution())

        # return "\n".join(solutions)

        # print "PlayGroundFields: {}".format(self.fields)
        # for field in self.fields:
        #     field.debug()
