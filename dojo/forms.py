# -*- coding: utf-8 -*-

from wtforms import Form, TextAreaField


TEXT = u"""
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


class SimpleForm(Form):
    text = TextAreaField(label='Text', default=TEXT)
