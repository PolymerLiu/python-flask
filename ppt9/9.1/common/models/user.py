# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
  __tablename__ = 'user'

  # Host = db.Column(db.String(60, 'utf8_bin'), primary_key=True, nullable=False, server_default=db.FetchedValue())
  # User = db.Column(db.String(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=db.FetchedValue())
  #
  # ssl_cipher = db.Column(db.LargeBinary, nullable=False)
  # x509_issuer = db.Column(db.LargeBinary, nullable=False)
  # x509_subject = db.Column(db.LargeBinary, nullable=False)
  # max_questions = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
  # max_updates = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
  # max_connections = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
  # max_user_connections = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
  # plugin = db.Column(db.String(64, 'utf8_bin'), nullable=False, server_default=db.FetchedValue())
  # authentication_string = db.Column(db.Text(collation='utf8_bin'))
  # password_last_changed = db.Column(db.DateTime)
  # password_lifetime = db.Column(db.SmallInteger)

  id = db.Column(db.Integer, primary_key=True, nullable=False, info='??')
  nickname = db.Column(db.String(30, 'utf8mb4_bin'), info='??')
  login_name = db.Column(db.String(20, 'utf8mb4_bin'), index=True, info='?????')
  login_pwd = db.Column(db.String(32, 'utf8mb4_bin'), primary_key=True, nullable=False, info='????')
  login_salt = db.Column(db.String(32, 'utf8mb4_bin'), primary_key=True, nullable=False, info='?????????')
  status = db.Column(db.Integer, server_default=db.FetchedValue(), info='?? 0??? 1???')
  update_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='????????')
  create_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='????')
