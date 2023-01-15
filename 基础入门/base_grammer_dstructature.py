## 语法和数据结构结构基础
### 注释，描述具体功能和怎么使用
# 单行注释，# 多行注释 “”“ ”“”
from numpy import conjugate

a = 1;
b = 2;
c = 3
print(a, b, c)

# 函数
"""
    封装一些独立的功能，可以直接调用
    与类和实例有绑定关系
    圆括号调用函数，传递零个或几个参数，或者将返回值给一个变量
"""
# 方法
"""
    方法必须依赖于类和对象进行调用
    与类和示例有绑定关系
    用点引用对象里附加的方法
"""

# 变量创建、赋值、参数传递
print("a=", a, "b=", b, "c=", c)

x = [1, 2, 3]
y = "Hello World!"

## 数据结构基础，字符串前＋ r 可以表示字符串中的 \ 不是转义字符
a = 12
b = 4
c = 5
print(a / b)

# python的布尔类型
# 复数
"""
    虚数不能单独存在，总是和一个值为0.0的实数部分一起构成一个复数
"""
cmp = 2 + 3j
print(cmp)

print("虚部：", cmp.imag)
print("实部：", cmp.real)

cmp_r = conjugate(cmp)  # 求共轭
print(cmp_r)

# #符号运算
import sympy as sbl
import math

math.pi
print("数值解", math.sin(math.pi))
print("解析解", sbl.sin(sbl.pi))

## 基础符号运算
from sympy import *

t, v0, g = symbols('t v0 g')  # symbols()声明符号变量
# rational(a,b)函数，生成有理数 a/b
y = v0 * t - Rational(1, 2) * g * t ** 2
dydt = diff(y, t)  # y对t求微分
print("一阶导数", dydt)
dydt2 = diff(dydt, t)
print("二阶导数", dydt2)
y2 = integrate(dydt, t)
print("对一阶导数积分：", y2)

# %%
from sympy import symbols

x = symbols('x', positive=True)  # 定义变量域为正
vars = symbols('x_1:5')  # x下标的范围是 x_1 x_2 x_3 x_4
print(vars)

# %%
import sympy as sy

x, y, z = symbols('x y z')
y = (x + 1) ** 2
print(expand(y))  # 展开函数
print(y.subs(x, 1))  # subs()方法，将符号函数的符号变量值换为1
# sympify() 字符串转符号表达式
st = 'x**2+2*x+1'
y = sympify(st)
print(y)

# simplify()化简
print(simplify(sin(x) ** 2 + cos(x) ** 2))
print(simplify(2 * sin(z) * cos(z)))

# %% 字符串变量
# 字符串：由  0  个或多个字符串组成的有序序列索引规则是从  0  开始
# 单引号，多引号，三引号都可以表示字符串
print('abcedef')
print('这是一对双引号""')
print("这是一个双引号\"\"")  # 尽量避免混合使用
# 字符串索引
name = "我的名字是韩善翔！"
print(name[::-1])  # 倒序索引，类似于matlab 最后一个为-1
# 回车(Carriage return) \r，换行（NEW LINE）\n 对于window是一样的

# 演示回车与换行
print("这段话演示\n换行转义符\n的作用")
print("~~~~~~~~~~~~~")
print("演示\r回车转义符\r的作用")
print("~~~~~~~~~~~~~")
print("这段话演示\b退格转义符\b的作用")

# 对字符串来说，*是复制 +是连接 x in y 判断x是否是y的一部分

# %% 小示例
weekstr = "一二三四五六日"
weekId = int(input("请输入一个星期数字（1-7）："))
print("星期" + weekstr[weekId - 1])

# Unicode->单字符 ：chr()函数
# 单字符->Unicode ord(x)函数

print("1+1=2" + chr(10004))

# %%字符串格式化
# {<参数序号>：<格式控制标记>}
# 格式化控制标记
# <填充> 用于填充的字符
# <对齐> < 左对齐 > 右对齐 ^ 居中对齐
# <宽度> 槽设定的输出宽度
# <，> 数字的千位分隔符
# <.精度> 浮点数小数精度或字符串最大输出长度
# <类型> 整数类型 b c d o x 浮点型 e f %
print("{0}:计算机{1}的CPU占用率为{2}".format('2020-1-1', 'C', '10'))
print("{:*^20,}".format(1234567))

# %%
# 字符串回顾
# strip() join()

# %% time库
import time

print(time.ctime())  # ctime()以易读方式显示
t = time.gmtime()  # 结构化时间，转换成计算机可以处理的时间
print(time.strftime("%Y-%m-%d %H:%M:%S", t))  # strftime()函数，按照想要的格式展示时间
# %%
start_time = time.perf_counter()  # 程序开始时间
sum = 0
for i in range(1000000):
    sum += i
end_time = time.perf_counter()
print(end_time - start_time)

# sleep()模拟休眠时间
# %% 实现进度条功能
import time

scale = 10
print("{:*^20}".format("执行开始"))
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("{:*^20}".format("执行结束"))

# %%静态进度条功能
import time

for i in range(101):
    # \r 回车符，将光标移到最前面
    print('\r{:3}%'.format(i), end="")
    time.sleep(0.1)
# %% 静态功能
import time

scale = 10
print("{:*^20}".format("执行开始"))
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    print('\r{:^3.0f}%[{}->{}]'.format(c, a, b), end="")  # end="" 指定不换行
    time.sleep(0.3)
print()
print("{:*^20}".format("执行结束"))
