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
        self.dimension = dimension
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
        self.debug()

    def walk_through_all_cells(self):
        for cell in self.todo:
            if cell[2] == '1':
                self.to_check.append(cell)

    def get_all_cells(self):
        row = 0
        for index, digit in enumerate("".join(self.content)):
            if not index == 0 and index % self.dimension == 0:
                row += 1

            self.todo.append((index % self.dimension, row, digit))


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
