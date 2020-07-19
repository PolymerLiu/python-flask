# 路由注册及web项目相关的事情

from application import app

# 引入debug tool
from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension(app)

# 拦截器处理和错误处理器
from interceptors.Auth import *
from interceptors.errorHandler import *

# 蓝图
from controllers.index import index_page
from controllers.member import member_page

app.register_blueprint(index_page,url_prefix='/')
app.register_blueprint(member_page,url_prefix='/member')