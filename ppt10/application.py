# 核心变量

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

import os

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:python123456@127.0.0.1/mysql"

# 传入flask去初始化一个db,即连接数据库
db = SQLAlchemy(app)

# 传入flask去初始化一个manager
manager = Manager(app)



app.config.from_pyfile("config/base_setting.py")
# ops_config=local|production
# Linux export ops_config=production
# windows set ops_config=local
