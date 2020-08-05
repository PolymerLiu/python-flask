from flask import Flask, Blueprint, render_template, request, jsonify
from common.libs.Helper import ops_renderJSON, ops_renderErrJSON
from common.libs.DateHelper import getCurrentTime
from common.models.user import User
from common.libs.UserService import UserService
from application import db
# app = Flask(__name__)

member_page = Blueprint('member_page', __name__)


@member_page.route('/reg', methods=['GET', 'POST'])
def reg():
  if request.method == 'GET': 
    return render_template('member/reg.html')

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
  print('-------------login_name',login_name)
  print('-------------user_info',user_info)
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


@member_page.route('/login')
def login():
  return render_template('member/login.html')
