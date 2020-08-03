from flask import Flask,Blueprint,render_template,request,jsonify

# app = Flask(__name__)

member_page = Blueprint('member_page',__name__)


@member_page.route('/reg')
def reg():
  return render_template('member/reg.html')

@member_page.route('/login')
def login():
  return render_template('member/login.html')
