from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps
from flask_blog.models.users import User
import bcrypt
import pdb


def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        try:
            user = User.query.filter_by(username=request.form['username']).first()
        except:
            flash('ユーザ名が異なります')
            return render_template('login.html')
        if request.form['username'] != user.username:
            flash('ユーザ名が異なります')
        elif bcrypt.hashpw(request.form['password'].encode(), user.salt.encode()).decode() != user.password:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            session['user_id'] = user.id
            flash('ログインしました')
            return redirect(url_for('entry.show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    flash('ログアウトしました')
    return redirect(url_for('entry.show_entries'))

@app.errorhandler(404)
def non_existant_route(error):
   return redirect(url_for('login'))