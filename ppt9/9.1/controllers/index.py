from flask import Flask, Blueprint, render_template
from common.models.user import User
from common.libs.Helper import ops_render

app = Flask(__name__)

index_page = Blueprint('index_page', __name__)


@index_page.route('/')
def index():
  name = 'imooc'
  context = {"name": name}
  context['user'] = {"nickname": "zaobana", "qq": "xxxxxx", "home_page": "http://www.54php.cn"}
  context['num_list'] = [1, 2, 3, 4, 5]

  # 查询数据库
  # ORM查询数据库
  result = User.query.all()
  context['result'] = result

  # 渲染模板，并通过上下文传入你想在模板里边渲染的数据
  return ops_render('index.html', context)
