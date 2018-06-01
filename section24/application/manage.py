from flask_script import Manager
from flask_blog import app

from flask_blog.scripts.db import InitDB


if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())
    manager.run()
