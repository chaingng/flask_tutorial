from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps
from flask import Blueprint

view = Blueprint('view', __name__)

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('view.login'))
        return view(*args, **kwargs)
    return inner


@view.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('entry.show_entries'))
    return render_template('login.html')


@view.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('entry.show_entries'))

@view.app_errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('view.login'))