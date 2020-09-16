# coding: utf-8
from application import db

class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='????')
    classify = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='??')
    actor = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='??')
    cover_pic = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='???')
    pics = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='????json')
    url = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='??????')
    desc = db.Column(db.Text, nullable=False, info='????')
    magnet_url = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='??????')
    hash = db.Column(db.String(32), nullable=False, unique=True, server_default=db.FetchedValue(), info='???')
    pub_date = db.Column(db.DateTime, nullable=False, index=True, info='????????')
    source = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='??')
    view_counter = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='???')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='??????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')

    def __init__(self,**items):
        for key in items:
            if hasattr(self,key):
                setattr(self,key,items[key])