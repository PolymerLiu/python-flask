# print ('hello python')
# print ('hello test')


# -*- coding: utf-8 -*-

print(45678 + 0x12fd2)
print(0x12fd2)
print(100 < 99)
print(0xff == 255)
print('康学习')

# 得到浮点数
print(11 / 4)
# 取整
print(11 // 4)
# 取余
print(11 % 4)

# 要解释上述结果，又涉及到 and 和 or 运算的一条重要法则：短路计算。

# 1. 在计算 a and b 时，如果 a 是 False，则根据与运算法则，整个结果必定为 False，因此返回 a；如果 a 是 True，则整个计算结果必定取决与 b，因此返回 b。

# 2. 在计算 a or b 时，如果 a 是 True，则根据或运算法则，整个计算结果必定为 True，因此返回 a；如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b

L = ['Adam', 95.5, 'lisa', 85, 'bart', 59]
# print (L)


L = ['Adam', 'Lisa', 'Bart']
# 末尾追加
L.append('Liu')
# 指定位置添加
L.insert(2, 'Jiafu')

# 末尾删除
L.pop()
# 指定位置删除
L.pop(2)

print(L)

# tuple元组  tuple一经生成就不能修改s
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# T中的数组是可以变的
T = ('a', 'b', ['A', 'B'])

print(t)

# if 语句
age = 7
if age >= 18:
  print('your age is', age)
print('adult')
