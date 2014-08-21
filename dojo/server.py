# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template


app = Flask(__name__)


NAVIGATION_BAR = [
    ('/', 'index', 'Index'),
    ('/task1', 'task1', 'Task1'),
    ('/task2', 'task2', 'Task2')
]


@app.route('/')
@app.route('/<app_name>')
def render(app_name=None):
    """
    Render the template of the given application or the index template.

    """
    context = {
        'navigation_bar': NAVIGATION_BAR,
    }

    if app_name:
        context['active_page'] = app_name
        return render_template('%s.html' % app_name, **context)

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.debug = True
    app.run()
