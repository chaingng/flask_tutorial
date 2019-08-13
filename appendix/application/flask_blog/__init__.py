from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

from flask_blog.views.entries import entry
from flask_blog.views.users import user

app.register_blueprint(entry, url_prefix='/users')
app.register_blueprint(user)

from flask_blog.views import views
