from flask import Flask,Blueprint
from indexcontroller import index_page

app = Flask(__name__)

app.register_blueprint(index_page,url_prefix='/imooc')
# app.register_blueprint(index_page,url_prefix='/post')



if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)

