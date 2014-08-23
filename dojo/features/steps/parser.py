# -*- coding: utf-8 -*-
from behave import *
import time

VALID_INPUT = u"""
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

INVALID_INPUT = u"""
schnick schnack schnick schnack schnick schnack schnick schnack schnick schnack
schnick schnackschnick schnackschnick schnackschnick schnack
1
schnuck
"""


@when('we visit the form and enter valid data')
def step1(context):
    context.browser.get('http://127.0.0.1:8000/task1')
    form = context.browser.find_element_by_id('text')
    form.send_keys(VALID_INPUT)
    form.submit()


@then('we see the solution')
def step2(context):
    solution = context.browser.find_element_by_css_selector('#solution pre')
    assert solution.text == "Beispieltext der ein paar Wrter"


@when('we visit the form and enter invalid data')
def step3(context):
    context.browser.get('http://127.0.0.1:8000/task1')
    form = context.browser.find_element_by_id('text')
    form.send_keys(INVALID_INPUT)
    form.submit()


@then('we see the error message')
def step4(context):
    solution = context.browser.find_element_by_css_selector('#solution pre')
    assert solution.text == "KEIN ABSCHNITT GEFUNDEN"
