from flask import Flask, Blueprint, render_template, request, jsonify
from common.libs.Helper import ops_renderJSON, ops_renderErrJSON

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

  return ops_renderJSON(msg='注册成功~~')


@member_page.route('/login')
def login():
  return render_template('member/login.html')
