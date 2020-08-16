from application import app
from flask import request,g
from common.models.user import User
from common.libs.UserService import UserService



@app.before_request
def before_request():
  # app.logger.info('-----before_request--------')
  user_info = check_login()
  g.current_user = None
  if user_info:
    g.current_user = user_info
  return


@app.after_request
def after_request(response):
  # app.logger.info('-----after_request--------')
  return response

# 判断用户是否登录
def check_login():
  # 通过request对象来获取cookie,客户端发起请求时会带上cookie
  cookies = request.cookies
  cookie_name = app.config['AUTH_COOKIE_NAME']
  auth_cookie = cookies[cookie_name] if cookie_name in cookies else None
  
  if auth_cookie is None:
    return False

  auth_info = auth_cookie.split('#')
  if len(auth_info) != 2:
    return False
  # 拿cookie里存储的ID查询是否有此用户
  try:
    user_info = User.query.filter_by(id = auth_info[1]).first()
  except Exception:
    return False

  # 拿cookie里的auth和用户信息生成的auth进行对比
  if auth_info[0] != UserService.geneAuthCode(user_info):
    return False
  return user_info