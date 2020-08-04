from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return 'hello flask'

# 如何启动服务
# 进入到index_1.py所在目录，set FLASK_APP=index_1.py
# flask run
