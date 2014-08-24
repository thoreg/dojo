# -*- coding: utf-8 -*-
import logging
import re
from collections import deque, defaultdict, namedtuple

Cell = namedtuple('Cell', 'x y value')
log = logging.getLogger('werkzeug')

IS_ONE_DIGIT = re.compile(r'\d$')


class Field:
    """
    Square field of '0's and '1's.

    """
    def __init__(self, dimension, field_lines):
        self.dimension = dimension
        self.content = field_lines
        self.todo = []

    def debug(self):
        print
        for index, cell in enumerate(self.todo):
            if index % self.dimension == 0:
                print "\n",
            print cell,

    def get_solution(self):
        self.get_all_cells()
        self.walk_through_all_cells()
        self.debug()

    def walk_through_all_cells(self):
        pass

    def get_all_cells(self):
        row = 0
        for index, digit in enumerate("".join(self.content)):
            if not index == 0 and index % self.dimension == 0:
                row += 1

            self.todo.append(Cell(x=index % self.dimension, y=row, value=digit))


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
