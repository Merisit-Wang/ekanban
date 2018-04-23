from . import db
from datetime import datetime
from config import type_list, priority_list

class Card(db.Model):
    __table_name__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    type = db.Column(db.Integer)
    priority = db.Column(db.Integer)
    expect_day = db.Column(db.Integer)
    start_time = db.Column(db.Date, default=datetime.utcnow())
    end_time = db.Column(db.Date, default=datetime.utcnow())
    actual_day = db.Column(db.Integer)
    author = db.Column(db.String(64))
    remark = db.Column(db.Text)

    @property
    def _type(self):
        for type in type_list:
            if type[0] == str(self.type):
                return type[1]
        return 'Type Error'

    @property
    def _priority(self):
        for priority in priority_list:
            if priority[0] == str(self.priority):
                return priority[1]
        return 'Priorty Error'

    def __repr__(self):
        return '<description %r>' %  self.description
