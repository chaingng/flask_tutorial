from flask_blog import db
from datetime import datetime

class Entry(db.Model):
    from flask_blog.models.users import User
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', foreign_keys=user_id)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None, user_id=None):
        self.title = title
        self.text = text
        self.user_id = user_id
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} title:{} text:{} user_id:{}>'.format(self.id, self.title, self.text, self.user_id)
