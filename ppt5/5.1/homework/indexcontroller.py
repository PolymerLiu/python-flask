from flask import Flask, Blueprint

app = Flask(__name__)

index_page = Blueprint('index_page', __name__)


@index_page.route('/index')
def index_page_index():
  return 'post index'


@index_page.route('/list')
def hello():
  return 'post list'
