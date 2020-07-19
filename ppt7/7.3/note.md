# 通过flask-sqlacodegen自动生成Model

pip install flask-sqlacodegen
用法
flask-sqlacodegen "mysql://root:python123456@127.0.0.1/mysql" --tables user --outfile "common/models/user.py" --flask

TODO
通过Model去生成数据库的一张表 

from common.models.user import User
db.create_all()