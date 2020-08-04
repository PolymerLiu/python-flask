from flask import Flask, Blueprint

app = Flask(__name__)

index_page = Blueprint('index_page', __name__)


@index_page.route('/')
def index_page_index():
  return 'index page'


@index_page.route('/me')
def hello():
  return 'my_page'
