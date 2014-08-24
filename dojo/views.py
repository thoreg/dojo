# -*- coding: utf-8 -*-

from dojo.forms import SimpleForm
from dojo.task1 import Parser
from dojo.task2 import PlayGround
from flask import flash, Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'really_very_secret'


NAVIGATION_BAR = [
    ('/', 'index', 'Index'),
    ('/task1', 'task1', 'Task1'),
    ('/task2', 'task2', 'Task2')
]


@app.route('/task2', methods=['GET', 'POST'])
def task2():
    app_name = "task2"
    description = "Bitte geben sie einen Text mit Spielfeldern ein"
    form = SimpleForm(request.form)
    context = {
        'active_page': app_name,
        'app_name': app_name,
        'description': description,
        'form': form,
        'navigation_bar': NAVIGATION_BAR,
    }
    if request.method == 'POST' and form.validate():
        playground = PlayGround(text=form.text.data)
        number_of_groups = [str(number_of_groups) for number_of_groups in playground.get_solution()]
        context['solution'] = "\n".join(number_of_groups)

    return render_template('task.html', **context)


@app.route('/task1', methods=['GET', 'POST'])
def task1():
    app_name = "task1"
    description = u"Bitte geben sie einen Text und die zu suchenden Wörter ein"
    form = SimpleForm(request.form)
    context = {
        'active_page': app_name,
        'app_name': app_name,
        'description': description,
        'form': form,
        'navigation_bar': NAVIGATION_BAR,
    }

    if request.method == 'POST' and form.validate():
        parser = Parser(text=form.text.data)
        parser.normalize()
        flash(u'Gesucht wird nach: {}'.format(parser.words))
        context['solution'] = parser.get_solution()

    return render_template('task.html', **context)


@app.route('/')
def index(app_name=None):
    return render_template('index.html', navigation_bar=NAVIGATION_BAR)


if __name__ == '__main__':
    app.run(debug=True)
