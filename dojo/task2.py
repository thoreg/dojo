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
        self.number_of_cells = self.dimension * self.dimension
        self.content = field_lines
        self.todo = []
        self.to_check = []

    def debug(self):
        print
        print "[todo]",
        for index, cell in enumerate(self.todo):
            if index % self.dimension == 0:
                print "\n",
            print cell,

        print "\n\n[to_check]"
        for cell in self.to_check:
            print cell

    def get_solution(self):
        self.get_all_cells()
        self.walk_through_all_cells()
        # self.debug()

    def walk_through_all_cells(self):
        # for cell in self.todo:
        #     print cell
        pass

    def get_all_cells(self):
        row = 0
        for index, digit in enumerate(range(self.number_of_cells)):
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
