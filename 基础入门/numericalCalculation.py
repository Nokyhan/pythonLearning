# %% 数值计算 利用计算机的强大运算功能
import random

print(random.random())

# %% 随机数种子
import random

x = random.getstate()  # 获取随机数种子
print(random.random())
random.setstate(x)
print(random.random())
# 在指定范围内生成随机数
print(random.uniform(10, 100))
b = [random.uniform(10, 100) for i in range(10)]
print(b)

# %% 使用循环计算生成随机数的标准差
import random as rd
from math import sqrt

sm = 0
sv = 0
i = 1
while i < 5000:
    a = rd.random()
    sm += a
    sv += a ** 2

    mean = sm / i
    smean = sqrt(sv / i - mean ** 2)

    i += 1
    if (i % 100) == 0:
        print(i, mean, smean)

# %% randint()生成随机整数
import random as rd


def six_eyes(N):
    S = 0
    for i in range(N):
        a = rd.randint(1, 6)
        if a == 6:
            S += 1
    return S, S / N


# %%　蒙特卡洛求骰子问题
import random as rd

N = 100000000
s = 0
for i in range(1, N):
    black = rd.randint(1, 6)
    red = rd.randint(1, 6)
    if black > red:
        s += 1
        if i % 1000000 != 0:
            continue
        print(s / N, black, red)

# %% 蒙特卡洛求pi近似值
import random as rd

N = 1000000
A = 0
for i in range(N):
    x = rd.uniform(-1, 1)
    y = rd.uniform(-1, 1)
    S = x ** 2 + y ** 2
    if S <= 1:
        A += 1
print(A / N * 4)

# %% 利用泰勒展开进行数值计算
import math

N = 5  # 计算次数
x = math.pi / 6  # 角度
sum = 0
for i in range(N):
    a = math.factorial(2 * i + 1)
    b = (-1) ** i * x ** (2 * i + 1) / a
    sum = sum + b
print(sum)

# %% 牛顿迭代法 收敛快
import math


def f(x):
    return (x - 3) ** 3


def fd(x):
    return 3 * ((x - 3) ** 2)


def newtonMethod(n, assum):  # n计数器 assume 假设的初值
    time = n
    x = assum
    Next = 0
    A = f(x)
    B = fd(x)
    print("A=" + str(A) + ',B=' + str(B) + ',time = ' + str(time))
    if f(x) == 0.0:
        return time, x
    else:
        Next = x - A / B
        print('Next x =' + str(Next))
    if abs(A - f(Next)) < 1e-6:
        print('Meet f(x) = 0,x= ' + str(Next))
    else:
        return newtonMethod(n + 1, Next)


newtonMethod(0, 4)

# %% python求解非线性方程


# %% 字典
dic = {'学号': '019', '姓名': '韩善翔', 'age': 19}
print(dic['学号'])
# %% 集合
set1 = {'哈哈哈', 19}
set2 = {'a', 'b', 'c', 'd'}
print(set1)
print(set1.union(set2))
set1.remove(19)
print(set1)


# %%案例
def getNum():
    nums = []
    isNumStr = input("请输入一个数字(回车退出)：")
    while isNumStr:  # 对输入的每一个数字都进行运算
        nums.append(isNumStr)
        isNumStr = input("请输入一个数字(回车退出):")
    return nums


def mean(numbers):  # 计算平均值
    numbers=[float(x) for x in numbers]
    s = 0.0  # 用来求和
    for num in numbers:
        s =s+ num
    return s / len(numbers)


def dev(numbers, mean):  # 计算标准差
    numbers = [float(x) for x in numbers]
    sdev = 0.0
    for num in numbers:
        sdev =sdev+ (num - mean) ** 2
    return pow(sdev / len(numbers) - 1, 0.5)


def median(numbers):
    numbers = [float(x) for x in numbers]
    new = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (new[size // 2 - 1] + new[size // 2]) / 2
    else:
        med = new[size // 2]
    return med


n = getNum()
print(n)
m=mean(n)
print("平均值：{}，标准差：{}，中位数：{}。".format(m,dev(n,m),median(n)))
