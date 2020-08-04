from werkzeug.wrappers import Request, Response


class Shortly(object):
  def __call__(self, environ, start_response):
    request = Request(environ)
    text = '<h1>Hello, World!%s</h1>' % (request.args.get('a', 'i love mooc'))
    response = Response(text, mimetype='text/html')
    return response(environ, start_response)

    # status = '200 ok'
    # headers = [('Content-Type', 'text/html; charset=utf8')]
    # start_response(status, headers)
    # return  ["b<h1>Hello, World!</h1>"]

    # start_response( '200 ok',[ ('Content-Type','text/plain') ] )
    # return [b'hello world']


if __name__ == '__main__':
  from werkzeug.serving import run_simple

  app = Shortly()
  run_simple('0.0.0.0', 5000, app)
