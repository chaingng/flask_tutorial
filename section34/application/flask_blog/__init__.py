from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_blog.config')

    db.init_app(app)

    from flask_blog.views.views import view
    app.register_blueprint(view)

    from flask_blog.views.entries import entry
    app.register_blueprint(entry, url_prefix='/users')

    return app