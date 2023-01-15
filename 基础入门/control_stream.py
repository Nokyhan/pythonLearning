## 控制流程
# 条件分支
# if
# if else
# if elif elif else
# 循环
# for循环
# while循环 break 跳出该层循环 continue 进入下一次循环
# %%

num = 20
flag = 3
while flag:  # 给三次机会
    guess = int(input("请输入一个整数："))
    flag -= 1
    if num == guess:
        print("恭喜你猜对了")
        break
    elif num > guess:
        print("猜小了！")
    else:
        print("猜大了！")
print("结束啦！")
# %% BMI值计算
height, weight = eval(input("请输入身高（m）和体重（kg）[逗号隔开]："))
bmi = weight / pow(height, 2)
print("BMI数值为：{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI 指标为：国际'{0}',国内'{1}'".format(who, nat))

# %%循环
print("九九乘法口诀表")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, "*", j, "=", i * j, end=" ")
    print()

# %% 函数，方便复用
# def 函数名(参数):
#      语句块
import math


def area(r):
    area = math.pi * r ** 2
    return area  # 带返回值的函数


def show(a, b):
    print('半径为', a, '圆的面积为', b, 'm^2')
    # 无返回值


A = area(5)
print(A)
show(5, A)

# %% 阶乘函数 函数内部为局部变量 如果想要参数内部为全局变量 可以使用global 保留字定义全局变量
n, s = 10, 100


def fact(n):
    s = 1
    for i in range(1, n + 1):
        s = s * i
    return s


print(fact(n), s)

# %% 匿名函数
# 定义方式
# lambda 参数：表达式

# %%调用外部函数
import congratulation
a="潘志"
b="姜珊"
congratulation.hhhshow(a,b)
