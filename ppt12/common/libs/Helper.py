from flask import jsonify,g,render_template
import math


def ops_render(template,context = {}):
  if 'current_user' in g:
    context['current_user'] = g.current_user
  return render_template(template,**context)

def ops_renderJSON(code=200, msg='操作成功~~', data={}):
  resp = {'code': code, 'msg': msg, 'data': data}
  return jsonify(resp)


def ops_renderErrJSON(msg='系统繁忙，请稍后再试~~', data={}):
  return ops_renderJSON(code=-1, msg=msg, data=data)

def iPagination(params):
  total_count = int(params['total_count'])
  page_size = int(params['page_size'])
  page = int(params['page'])
  url = params['url']

  total_pages = math.ceil(total_count/page_size)
  total_pages = total_pages if total_pages>0 else 1

  is_prev = 0 if page <= 1 else 1
  is_next = 0 if page >= total_pages else 1

  pages={
    'page_size':page_size,
    'total':total_count,
    'total_pages':total_pages,
    'range':range(1,total_pages+1),
    'is_prev':is_prev,
    'is_next':is_next,
    'current':page,
    'url':url,
  }
  
  return pages
