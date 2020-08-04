from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return 'hello,i love imooc'


@app.route('/my/<username>')
def myname(username):
  return 'my page %s' % (username)


@app.route('/my')
def my():
  return 'my page'


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
