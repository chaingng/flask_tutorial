from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db
from flask_blog.models.users import User
from flask_blog.views.views import login_required
from flask import Blueprint
import pdb

user = Blueprint('user', __name__)


@user.route('/users', methods=['POST'])
def add_user():
    user = User(
            username=request.form['username'],
            password=request.form['password']
            )
    db.session.add(user)
    db.session.commit()
    flash('新規ユーザ登録が完了しました。ログインしてください。')
    return redirect(url_for('login'))


@user.route('/users/new', methods=['GET'])
def new_user():
    return render_template('users/new.html')