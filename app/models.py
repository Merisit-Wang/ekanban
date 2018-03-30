from . import db
from datetime import datetime

class Card(db.Model):
    __table_name__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    type = db.Column(db.Integer)
    priority = db.Column(db.Integer)
    expect_day = db.Column(db.Integer)
    start_time = db.Column(db.DateTime, default=datetime.utcnow())
    end_time = db.Column(db.DateTime, default=datetime.utcnow())
    actual_day = db.Column(db.Integer)
    author = db.Column(db.Integer)
    remark = db.Column(db.Text)

    def __repr__(self):
        return '<description %r>' %  self.description
