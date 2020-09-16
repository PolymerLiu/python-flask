from flask import Flask, Blueprint, render_template,request,redirect
from common.models.movie import Movie
from common.libs.Helper import ops_render,iPagination
from common.libs.UrlManager import UrlManager
import math
from sqlalchemy.sql.expression import func
from application import db

app = Flask(__name__)

index_page = Blueprint('index_page', __name__)


@index_page.route('/')
def index():
  req = request.values
  order_by_f = str(req['order']) if ('order' in req and req['order'] ) else 'lastest'
  page = 1
  if 'p' in req and req['p']:
    page = int(req['p'])

  query = Movie.query

  page_params = {
    'total_count':query.count(),
    'page_size':30,
    'page':page,
    'url':'/?',
  }
  pages = iPagination(page_params)

  # 0-30,30-60,60-90
  offset = (page - 1) * page_params['page_size']
  limit = page * page_params['page_size']

  if order_by_f == 'hot':
    query = query.order_by(Movie.view_counter.desc(),Movie.id.desc())
  else:
    query = query.order_by(Movie.pub_date.desc(),Movie.id.desc())
  list_movie = query[offset:limit]

  # 渲染模板，并通过上下文传入你想在模板里边渲染的数据
  return ops_render('index.html', {"data":list_movie,"pages":pages})

@index_page.route('/info')
def info():
  req = request.values
  id = int(req['id']) if ('id' in req and req['id']) else 0
  if id<1:
    return redirect(UrlManager.buildUrl('/'))
  info = Movie.query.filter_by(id=id).first()

  if not info:
    return redirect(UrlManager.buildUrl('/'))

  # 获取随机推荐，从数据库随机查询4条数据
  recommend_list = Movie.query.order_by(func.rand()).limit(4)

  # 更新阅读数量
  info.view_counter +=1
  db.session.add(info)
  db.session.commit()

  return ops_render("info.html",{'info':info,'recommend_list':recommend_list})
