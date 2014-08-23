# -*- coding: utf-8 -*-
from dojo.parser import Parser

INPUT = u"""
Ein toller Beispieltext ist Blindtext. Er hat ein paar Wörter. Dies ist ein
Beispieltext, der ein paar Wörter hat und auch noch ein paar mehr, um die
Zeile etwas länger zu machen. Darüber hinaus ist er nur dafür da, um
genügend Testtext zusammenzubekommen. Dem Text selbst macht das nicht so
viel aus. Früher einmal mehr, als er noch nicht so selbstbewusst war. Heute
kennt er seine Rolle als Blindtext und fügt sich selbstbewusst ein. Er ist
ja irgendwie wichtig. Manchmal jedoch, ganz manchmal, weint er in der Nacht,
weil er niemals bis zum Ende gelesen wird. Doch das hat ja jetzt zum Glück
ein Ende.
5
ein
Beispieltext
der
paar
Wörter
"""

EXPECTED_TEXT = u"""
Ein toller Beispieltext ist Blindtext. Er hat ein paar Wörter. Dies ist ein
Beispieltext, der ein paar Wörter hat und auch noch ein paar mehr, um die
Zeile etwas länger zu machen. Darüber hinaus ist er nur dafür da, um
genügend Testtext zusammenzubekommen. Dem Text selbst macht das nicht so
viel aus. Früher einmal mehr, als er noch nicht so selbstbewusst war. Heute
kennt er seine Rolle als Blindtext und fügt sich selbstbewusst ein. Er ist
ja irgendwie wichtig. Manchmal jedoch, ganz manchmal, weint er in der Nacht,
weil er niemals bis zum Ende gelesen wird. Doch das hat ja jetzt zum Glück
ein Ende."""


def test_read_input():
    parser = Parser(text=INPUT)
    assert parser.text == EXPECTED_TEXT
    assert parser.words == [u'ein', u'Beispieltext', u'der', u'paar', u'W\xf6rter']


def test_normalize_text():
    parser = Parser(text="12! 123.   3,o  5  ass?")
    parser.normalize()
    assert parser.text == ' o ass'


def test_normalize_words():
    parser = Parser()
    parser.words = ["12!", "123.", "3,o", "5  s?"]
    parser.normalize()
    assert parser.words == ['o', 's']


def test_get_rarest_word():
    parser = Parser()
    parser.words = ['aaa', 'bbb', 'ccc', 'ddd']
    parser.word_indicies = {
        'aaa': [1, 2, 3],
        'bbb': [4, 5],
        'ccc': [6],
        'ddd': [7],
    }
    print parser.get_rarest_word()


# Fails with multiple rarest words ...
def _test_get_solution():
    parser = Parser(text=INPUT)
    parser.normalize()
    solution = parser.get_solution()

    assert solution == "Beispieltext der ein paar Wrter"
