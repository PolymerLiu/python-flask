# 路由注册及web项目相关的事情

from application import app
from indexcontroller import index_page

app.register_blueprint(index_page, url_prefix='/')
# app.register_blueprint(index_page,url_prefix='/post')
