from flask import Flask, Blueprint, request, jsonify,make_response,redirect
from common.libs.Helper import ops_renderJSON, ops_renderErrJSON
from common.libs.DateHelper import getCurrentTime
from common.models.user import User
from common.libs.UserService import UserService
from common.libs.UrlManager import UrlManager
from application import db,app
from common.libs.Helper import ops_render

member_page = Blueprint('member_page', __name__)


@member_page.route('/reg', methods=['GET', 'POST'])
def reg():
  if request.method == 'GET': 
    return ops_render('member/reg.html')

  req = request.values
  login_name = req['login_name'] if 'login_name' in req else ''
  login_pw1 = req['login_pw1'] if 'login_pw1' in req else ''
  login_pw2 = req['login_pw2'] if 'login_pw2' in req else ''

  if login_name is None or len(login_name) < 1:
    return ops_renderErrJSON(msg='请输入正确的用户名~~')

  if login_pw1 is None or len(login_pw1) < 6:
    return ops_renderErrJSON(msg='请输入正确的登录密码~~，并且长度不能小于6个字符')

  if login_pw2 != login_pw1:
    return ops_renderErrJSON(msg='请输入正确的确认密码~~')

  # 登录用户名校验
  user_info = User.query.filter_by(login_name=login_name).first()
  if user_info:
    return ops_renderErrJSON(msg='此用户名已经存在，请换一个~~')

  model_user = User()
  model_user.login_name = login_name
  model_user.nickname = login_name
  model_user.login_salt = UserService.geneSalt(8)
  model_user.login_pwd = UserService.genePwd(login_pw1,model_user.login_salt)
  model_user.create_time = model_user.update_time = getCurrentTime()
  # 往数据库插入数据
  db.session.add(model_user)
  db.session.commit()

  return ops_renderJSON(msg='注册成功~~')


@member_page.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return ops_render('member/login.html')

  # 登录判断
  req = request.values
  login_name = req['login_name'] if 'login_name' in req else ''
  login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

  if login_name is None or len(login_name) < 1:
    return ops_renderErrJSON(msg='请输入正确的用户名~~')

  if login_pwd is None or len(login_pwd) < 6:
    return ops_renderErrJSON(msg='请输入正确的登录密码~~，并且长度不能小于6个字符')
  

  # 登录校验
  user_info = User.query.filter_by(login_name=login_name).first()
  print('user_info',user_info)
  print('login_name',login_name)
  if not user_info:
    return ops_renderErrJSON(msg='请输入正确的登录用户名和密码 -1 ~~')

  if user_info.login_pwd != UserService.genePwd(login_pwd,user_info.login_salt):
    return ops_renderErrJSON(msg='请输入正确的登录用户名和密码 -2 ~~')

  if user_info.status != 0:
    return ops_renderErrJSON(msg='账号被禁用，请联系管理员处理 ~~')

  # session['uid'] = user_info.id
  response = make_response( ops_renderJSON(msg='登录成功~~') )
  # 把跟用户相关的信息和用户ID存储到cookie中，并用#分隔
  response.set_cookie(app.config['AUTH_COOKIE_NAME'],"%s#%s"%(UserService.geneAuthCode(user_info),user_info.id),60*60*24*120)

  return response

@member_page.route('/logout')
def logOut():
  response = make_response(redirect(UrlManager.buildUrl("/")))
  response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
  return response

