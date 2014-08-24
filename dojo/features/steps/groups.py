# -*- coding: utf-8 -*-
from behave import *

INPUT_NORMAL = u"""4
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

INPUT_EXTREME = u"""2
4
0000
0000
0000
0000
4
1111
1111
1111
1111
"""


@when('we visit the form of task2 and enter valid data')
def step1(context):
    context.browser.get('http://127.0.0.1:8000/task2')
    form = context.browser.find_element_by_id('text')
    form.send_keys(INPUT_NORMAL)
    form.submit()


@then('we see the solution for task2')
def step2(context):
    solution = context.browser.find_element_by_css_selector('#solution pre')
    assert solution.text == "1\n3\n3\n9"


@when('we visit the form of task2 and enter valid extreme data')
def step3(context):
    context.browser.get('http://127.0.0.1:8000/task2')
    form = context.browser.find_element_by_id('text')
    form.send_keys(INPUT_EXTREME)
    form.submit()


@then('we see the solution for extreme task2')
def step4(context):
    solution = context.browser.find_element_by_css_selector('#solution pre')
    assert solution.text == "0\n1"
