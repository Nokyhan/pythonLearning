# 循环语句
# whlie
while True:
    print('Hello!')
    answer = input('是否退出循环？')
    if answer == '是':
        break

# break 跳出循环
# continue 跳出本次循环，进入下一次
# while 搭配else 可以检测循环情况
day: int = 1
while day <= 7:
    answer = input('你今天有好好学习嘛？')
    if answer != '有':
        break
    else:
        day += 1
else:
    print("非常棒！！！")

# 9*9乘法口诀表
i: int = 1
while i <= 9:
    j: int = 1
    while j <= i:
        print(j, '*', i, '=', i * j, end=" ")  # end=" " 是为了加个空格 让不同输出之间有间隔
        j += 1
    i += 1
    print()

# for 循环
# for 变量 in 可迭代对象：
# statement(s)
for each in 'NOKY':
    print(each)

# range(m)函数 生成从 o 开始 到 m的序列 ，不包括 m
# range(start,end) 从start开始，end结束，左闭右开
# range(start,end,step)                        ,step为step
sum = 0
# 从0 加到 99
for i in range(100):
    sum += i
print(sum)

# 输出10以内素数


for m in range(2, 10):
    flag = 1  # 设置标志位
    # 循环用来判断 m是否可以被其他数整除
    for x in range(2, int(m / 2)+1):
        if m % x == 0:
            flag = 0
    if flag == 1:
        print(m, end=" ")
