from flask import Flask

app = Flask(__name__)


# @app.route('/')
def hello():
  return 'hello,i love imooc'


# @app.route('/my/<username>')
def myname(username):
  return 'my page %s' % (username)


app.add_url_rule(rule='/', view_func=hello)
app.add_url_rule(rule='/my/<username>', view_func=myname)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
