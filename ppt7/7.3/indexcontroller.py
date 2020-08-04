from flask import Flask, Blueprint, request, make_response, jsonify, render_template
from sqlalchemy import text
from application import db
from common.models.user import User

app = Flask(__name__)

index_page = Blueprint('index_page', __name__)


@index_page.route('/')
def index_page_index():
  return 'index page'


@index_page.route('/template')
def template():
  name = 'imooc'
  context = {"name": name}
  context['user'] = {"nickname": "zaobana", "qq": "xxxxxx", "home_page": "http://www.54php.cn"}
  context['num_list'] = [1, 2, 3, 4, 5]

  # 查询数据库 
  # sql = text("select * from `user`")
  # result = db.engine.execute(sql)

  # 查询数据库
  # ORM查询数据库
  result = User.query.all()
  context['result'] = result

  # return render_template('index.html',name = name)
  return render_template('index.html', **context)


@index_page.route('/extend_template')
def extend_template():
  return render_template('extend_template.html')
