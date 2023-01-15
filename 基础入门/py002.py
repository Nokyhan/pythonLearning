### 用python写的小游戏 ###
import random

# random随机数函数
# 生成一个在1~10之间的随机数
num = random.randint(1, 10)

counts = 3
while counts > 0:
    temp = input("猜一猜小甲鱼现在心里想的是哪个数字：")
    guess = int(temp)
    if guess == num:
        print("你是小甲鱼肚里的蛔虫吗？")
        print("猜中了也没奖励！")
        break
    else:
        if guess < num:
            print('小啦')
        if guess > num:
            print("大啦")
    counts = counts - 1  # 相当于设置只有三次机会
print("游戏结束！")