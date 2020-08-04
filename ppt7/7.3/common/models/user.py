# coding: utf-8
# 已经完成了数据库表结构的设计，通过flask-sqlacodegen这个库生成对应的model
from application import db


class User(db.Model):
  __tablename__ = 'user'

  Host = db.Column(db.String(60, 'utf8_bin'), primary_key=True, nullable=False, server_default=db.FetchedValue())
  User = db.Column(db.String(32, 'utf8_bin'), primary_key=True, nullable=False, server_default=db.FetchedValue())

  ssl_cipher = db.Column(db.LargeBinary, nullable=False)
  x509_issuer = db.Column(db.LargeBinary, nullable=False)
  x509_subject = db.Column(db.LargeBinary, nullable=False)
  max_questions = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
  max_updates = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
  max_connections = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
  max_user_connections = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
  plugin = db.Column(db.String(64, 'utf8_bin'), nullable=False, server_default=db.FetchedValue())
  authentication_string = db.Column(db.Text(collation='utf8_bin'))
  password_last_changed = db.Column(db.DateTime)
  password_lifetime = db.Column(db.SmallInteger)
