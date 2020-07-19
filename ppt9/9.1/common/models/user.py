# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, nullable=False, info='??')
    nickname = db.Column(db.String(30, 'utf8mb4_bin'), info='??')
    login_name = db.Column(db.String(20, 'utf8mb4_bin'), index=True, info='?????')
    login_pwd = db.Column(db.String(32, 'utf8mb4_bin'), primary_key=True, nullable=False, info='????')
    login_salt = db.Column(db.String(32, 'utf8mb4_bin'), primary_key=True, nullable=False, info='?????????')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='?? 0??? 1???')
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='????????')
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='????')
