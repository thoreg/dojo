# -*- coding: utf-8 -*-

from wtforms import Form, TextAreaField

TEXT = """
4
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

class SimpleForm(Form):
    text = TextAreaField(label='Text', default="TEXT")
