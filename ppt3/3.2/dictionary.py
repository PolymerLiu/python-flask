# 列表是有序的对象集合，通过下标来获取元素
# 字典是无序的对象集合，通过key来获取元素
# 字典用{}来标识，是一个无序的key:value集合
# key必须使用不可变类型，在同一个字典中，key是唯一的

if __name__ == '__main__':
  dict = {}
  dict['first'] = 1
  dict[2] = '2'

  tinydict = {'name':'jeffrey','age':18,'sex':'man'}

  print(dict['first'])
  print(dict[2])

  print(tinydict.keys())  #输出所有的key
  print(tinydict.values())  #输出所有的值
