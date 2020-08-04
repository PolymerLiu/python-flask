# 启动文件

from application import app
from www import *

if __name__ == "__main__":
  app.run(host='localhost', debug=True)
