# 路由注册及web项目相关的事情

from application import app
from controllers.index import index_page

# 引入debug tool
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension(app)

# 拦截器处理和错误处理器
from interceptors.Auth import *
from interceptors.errorHandler import *

app.register_blueprint(index_page, url_prefix='/')
