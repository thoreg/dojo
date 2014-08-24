# -*- coding: utf-8 -*-
import re
import logging
from collections import deque, defaultdict, namedtuple

Result = namedtuple('Result', 'distance begin end')
log = logging.getLogger('werkzeug')

is_one_digit = re.compile(r'\d$')
regex_text = re.compile(r'[^a-zA-Z\s]')
multiple_white_spaces = re.compile(r'\s+')


class Parser:
    """
    Class to find out the shortest earliest range in a given text, which contains the given words.

    """
    def __init__(self, text=''):
        self.word_indicies = defaultdict(list)
        self.words = []
        text_lines = []

        is_text = True
        for line in text.splitlines():

            if is_one_digit.match(line):
                is_text = False
                continue

            if is_text:
                text_lines.append(line)
            else:
                self.words.append(line)

        self.text = "\n".join(text_lines)
        self.words = self.words

    def normalize(self):
        """
        Normalize a string means here: Remove everything but characters.
        Remove empty elements from the normalized result.

        """
        self.text = regex_text.sub('', self.text)
        self.text = multiple_white_spaces.sub(' ', self.text)

        self.words = [regex_text.sub('', word) for word in self.words]
        self.words = [multiple_white_spaces.sub('', word) for word in self.words]
        self.words = filter(None, self.words)

    def _get_positions_of_each_word_in_text(self, text):
        """
        Store the index of each word within the text in a dictionary. The key is the word.

        """
        indicies = defaultdict(list)
        for index, term in enumerate(text.split()):
            indicies[term].append(index)
        return indicies

    def get_solution(self):
        """
        Algorithm:
        - find all indicies for all words within the text
        - find out which words are the rarest
        - for each of the rarest words find out the smallest sum of the distances of each nearest
          occurence (absolute value) of each other word from the list of words to search for
        - collect for each rarest word the sum of all distances, the begin and the and of the range
          which contains all words
        - return the smallest distance with the smallest value for begin

        """
        self.word_indicies = self._get_positions_of_each_word_in_text(self.text)

        if not self.words:
            return u"ES KONNTEN KEINE WÖRTER IDENTIFIZIERT WERDEN"

        if not self.each_word_found():
            return u"KEIN ABSCHNITT GEFUNDEN"

        self.rarest_words = self.get_rarest_words()
        log.info("\nThe rarest words: {}".format(self.rarest_words))

        results = []
        for word in self.rarest_words:
            result = self.get_distance_begin_and_end(word)
            log.info("\nResult: {}\n".format(result))
            results.append(result)

        result = sorted(results)[0]
        log.info("Results: {}".format(sorted(results)))

        return " ".join(self.text.split()[result.begin:result.end])

    def get_distance_begin_and_end(self, word):
        """
        Find the nearest 'indicies' of the other 'search_words' based on the rarest search_word.
        Sum up the distance for each search_word over all search word indicies. Do this for every
        index of the rarest search word and return the begin and the end of the nearest indicies.

        """
        list_of_search_words = list(self.words)
        list_of_search_words.remove(word)
        result = {}

        result_distance = None

        for index in self.word_indicies[word]:
            distance = 0
            begin = 0
            end = 0

            log.info("\nDiscover '{}' at index: {}".format(word, index))
            for search_word in list_of_search_words:
                nearest_index = self.find_nearest_value_in_a_list(index,
                                                                  self.word_indicies[search_word])
                log.info("'{}'' nearest value to {} is {}".format(
                         search_word,
                         index,
                         nearest_index))

                if begin == 0:
                    begin = nearest_index

                begin = min(begin, nearest_index)
                end = max(end, nearest_index)
                distance += self.get_distance(index, nearest_index)

            log.info("distance: {} begin: {} end: {}".format(distance, begin, end))

            if result_distance is None or distance < result_distance:
                result = Result(distance, begin, end + 1)
                result_distance = distance

        return result

    def find_nearest_value_in_a_list(self, value, list_to_browse):
        """
        Return the value of a list which is the nearest to a given value.

        """
        index_of_the_nearest_value = min(range(len(list_to_browse)),
                                         key=lambda i: abs(list_to_browse[i]-value))
        return list_to_browse[index_of_the_nearest_value]

    def get_distance(self, value_a, value_b):
        """
        Return the distance between two given values.

        """
        return abs(int(value_a) - int(value_b))

    def get_rarest_words(self):
        """
        Return a list of words which have the shortest list of occurrence (inicies) within the text.

        """
        rarest_words = deque()
        occurrence = 0
        for word in self.words:
            if occurrence == 0:
                occurrence = len(self.word_indicies[word])
                rarest_words.append((word, occurrence))

            elif occurrence > len(self.word_indicies[word]):
                occurrence = len(self.word_indicies[word])
                rarest_words.clear()
                rarest_words.append((word, occurrence))

            elif occurrence == len(self.word_indicies[word]):
                rarest_words.append((word, occurrence))

            log.info("\"{}\" occures {} times in {}".format(
                     word,
                     len(self.word_indicies[word]),
                     self.word_indicies[word]))

        return [word[0] for word in rarest_words]

    def each_word_found(self):
        """
        Return true if each word of the words to search for was found in the text.

        """
        for word in self.words:
            if not word in self.word_indicies:
                return False

        return True
