# def bar():
#   logging('bar1','12')
#   print('im a bar')

# def bar2():
#   logging('bar2',16)
#   print('im a bar')

# def logging(name,sex):
#   # print('debug '+name+' is running')
#   print('debug %s %s is running' %(name,sex))

# bar()
# bar2()

# 函数装饰器
def logging(func):
  def inner(*args, **kwargs):
    print('debug %s is running' % func.__name__)
    return func(*args, **kwargs)

  return inner


@logging
def bar():
  print('im a bar')


@logging
def bar2():
  print('im a bar')


# bar = logging(bar)
bar()
# bar2 = logging(bar2)
bar2()
