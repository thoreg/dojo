# -*- coding: utf-8 -*-
import logging

log = logging.getLogger('werkzeug')


class Field:
    """
    Square field of '0's and '1's.

    """
    def __init__(self, dimension, field_lines):
        self.dimension = int(dimension)
        self.content = field_lines
        self.todo = []

    def get_solution(self):
        self.setup_cells()
        return self.get_number_of_groups()

    def get_number_of_groups(self):
        """
        Walk through the whole field and count the groups of '1' which are connected.
        Connected means here these 'cells' are neighbours via N/NO/O/OS/S/SW/W/NW.

        """
        log.info("self.content: {}".format(self.content))
        log.info("todo: ".format(self.todo))

        number_of_groups = 0
        seen = set()
        to_check = set()

        while self.todo:
            x, y = self.todo.pop()
            if (x, y) in seen:
                continue

            if self.content[y][x] == '0':
                seen.add((x, y))
                continue

            log.info("\nNew Cell to check found: ({}, {})".format(x, y))
            to_check.add((x, y))
            number_of_groups += 1

            while to_check:
                (x, y) = to_check.pop()
                if (x, y) in seen:
                    log.info("   cell {} already seen".format((x, y)))
                    continue

                neighbours = self.get_neighbours_of_cell(x, y)
                log.info("   neighbours: {}".format(neighbours))
                for nx, ny in neighbours:
                    if self.content[ny][nx] == '1':
                        to_check.add((nx, ny))

                seen.add((x, y))

        log.info("Number_of_groups: {}".format(number_of_groups))
        return number_of_groups

    def setup_cells(self):
        """
        Build a matrix with all coordinates for all cells of the field.

        """
        self.todo = []
        for y in range(self.dimension):
            for x in range(self.dimension):
                self.todo.append((x, y))

    def get_neighbours_of_cell(self, x, y):
        """
        Return a list of tuples with the coordinates of all neighbours of the cell at (x, y).

        ---------------
        | NW | N | NO |
        ---------------
        |  W | x |  O |
        ---------------
        | SW | S | SO |
        ---------------

        """
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
        if (x, y) in neighbours:
            neighbours.remove((x, y))

        return sorted(neighbours)


class PlayGround:
    """
    A playground consists of sevral Field objects.

    """
    def __init__(self, text=''):
        self.fields = []
        for line_number, line in enumerate(text.splitlines()):
            if line_number == 0:
                continue

            # A new field begins
            if line.isdigit():
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

        return solutions
