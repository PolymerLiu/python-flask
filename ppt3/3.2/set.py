if __name__ == '__main__':

  emptyset = set()
  student = {'tom','jack','simmon','tag','dog','cat','tom'}
  print(student) # 输出集合，重复的元素会被自动去掉

  if 'simmon' in student:
    print('simmon 在集合中')
  else:
    print('simmon bu在集合中')

  # set可以进行集合运算
  a = set('asjdosfosdajslkf')
  b = set('erieeierrifre')

  # a和b的差集
  print(a-b)

  # a和b的并集
  print(a|b)

  # a和b的交集
  print(a&b)

  # a和b中不同时存在的元素
  print(a^b)