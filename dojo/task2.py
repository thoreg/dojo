# -*- coding: utf-8 -*-
import re
import logging
from collections import deque, defaultdict, namedtuple

Result = namedtuple('Result', 'distance begin end')
log = logging.getLogger('werkzeug')

is_one_digit = re.compile(r'\d$')
regex_text = re.compile(r'[^a-zA-Z\s]')
multiple_white_spaces = re.compile(r'\s+')


class Field:
    """
    Square field of '0's and '1's.

    """
    def __init__(self, dimension, field_lines):
        self.dimension = dimension
        self.content = field_lines

    def debug(self):
        print "\n{} x {}".format(self.dimension, self.dimension)
        for line in self.content:
            print "{}".format(line)


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
            if is_one_digit.match(line):
                dimension = int(line)
                field_lines = []
                lines_left = dimension
                continue

            if lines_left:
                field_lines.append(line)
                lines_left -= 1
                if lines_left == 0:
                    self.fields.append(Field(dimension, field_lines))


        # print "PlayGroundFields: {}".format(self.fields)
        # for field in self.fields:
        #     field.debug()
