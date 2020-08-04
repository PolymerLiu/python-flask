# 核心变量

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 初始化DB配置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:python123456@127.0.0.1/mysql"

# 传入flask去初始化一个db,即连接数据库
db = SQLAlchemy(app)
