import random
# 变量和字符串
x = 5
y = 3
# 非常优雅的交换了字符值
y, x = x, y
print('x=', x)
print('y=', y)

# 转义字符 \+字符
print('hello\nworld')
print('D:\\hh\\h1')
print(r'D:\H\H1')

# 三个“”“ ”“” 可以随意换行
print(""" ***
*****
***
""")

# 字符串运算
print(520 + 1314)
print('520' + '1314')
print('我每天爱你三千遍！\n'*100)

#随机数种子，通过获取随机数，可重现生成的伪随机数
x = random.getstate()
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))

# 使用刚刚的伪随机数种子,复现生成的伪随机数
random.setstate(x)
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
