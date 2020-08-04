from flask import Flask, Blueprint, request

app = Flask(__name__)

index_page = Blueprint('index_page', __name__)


@index_page.route('/')
def index_page_index():
  return 'index page'


@index_page.route('/me')
def hello():
  return 'my_page'


@index_page.route('/get')
def get():
  # var_a = request.args.get('a','i love imooc')
  req = request.values
  var_a = req['a'] if 'a' in req else 'i love imooc get'
  return 'request:%s,params:%s,var_a:%s' % (request.method, request.args, var_a)


@index_page.route('/post', methods=['POST'])
def post():
  # var_a = request.form['a'] if 'a' in request.form else post ''
  req = request.values
  var_a = req['a'] if 'a' in req else 'i love imooc post'
  return 'request:%s,params:%s,var_a:%s' % (request.method, request.form, var_a)


@index_page.route('/upload', methods=['POST'])
def upload():
  # post 上传文件，enctype="multipart/form-data"
  f = request.files['file'] if 'file' in request.files else None
  return 'request:%s,params:%s,file:%s' % (request.method, request.files, f)
