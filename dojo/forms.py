# -*- coding: utf-8 -*-

from wtforms import Form, TextAreaField


class SimpleForm(Form):
    text = TextAreaField(label='Text', default="Bitte geben Sie hier Ihre Daten ein")
