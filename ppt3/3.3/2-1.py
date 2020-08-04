# 带参数的函数装饰器
def logging(level='one'):
  def decorator(func):
    def inner(*args, **kwargs):
      print(' %s %s is running' % (level, func.__name__))
      return func(*args, **kwargs)

    return inner

  return decorator


@logging('info')
def bar():
  print('im a bar')


bar()
