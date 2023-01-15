# 序列
# 可以通过索引获得元素
#  第一个元素syzwei0
# 通过切片获得集合
# 共同的运算符

## 运算符与函数
# + ：序列进行拼接（对于可变序列，在原序列进行修改 不可变序列，则生成新的）
# *：序列进行重复
# del 语句，用于删除一个或多个对象
x=['1','2','3','4','5','6']
del x[1:3]
print(x)

# 与可迭代对象相关的函数
# 列表、元组和字符串相互转换
temp=list("NOKY")
print(temp)
temp=(1,2,3,4,5)
# 将元组转换为列表 list()
temp=list(temp)
print(temp)

# 将列表转换为元组 tuple()
temp=tuple(temp)
print(temp)

# 将可迭代对象转换为字符串 str()
print("转换为字符串：",str(temp))

#min() max() 找出最大值，最小值
# sorted() 对元组、列表和字符串都可以进行排序
# all()函数 判断对象是否所有都为真
# any()
# enumerate() 返回一个枚举对象，使用
seasons=['spring','summer','fall','winter']
print(list(enumerate(seasons)))
# zip()函数，对应位置元素组合起来
x=[1,2,3]
y=[4,5,6]
z=[7,8,9]
zipped=zip(x,y,z)
print(list(zipped))

# map() 第一个参数指定操作，第二个参数为需要操作的迭代对象
mapped=map(pow,[1,2,3],[1,2,3])
print(list(mapped))
# filter() 过滤器，在第二个参数中过滤满足第一个元素的

# 一个迭代器就是一个可迭代对象，迭代器只能使用一次
# iter() 将可迭代对象转换成迭代器
