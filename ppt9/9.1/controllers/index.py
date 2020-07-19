from flask import Flask,Blueprint,render_template
from common.models.user import User

app = Flask(__name__)

index_page = Blueprint('index_page',__name__)


@index_page.route('/')
def index():
  name = 'imooc'
  context = {"name":name}
  context['user'] = {"nickname":"zaobana","qq":"xxxxxx","home_page":"http://www.54php.cn"}
  context['num_list'] = [1,2,3,4,5]

  # 查询数据库
  # ORM查询数据库
  result = User.query.all()
  context['result'] = result

  return render_template('index.html',**context)
