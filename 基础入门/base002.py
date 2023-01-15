# 数据类型
# decimal 十进制
import decimal as dec

a = dec.Decimal('0.1')
b = dec.Decimal('0.2')
c = dec.Decimal('0.3')
print(c == a + b)
print(0.00005)
x = 1+2j
print('x的实部',x.real)
print('x的虚部',x.imag)

# 3 //5 (地板除) 取比目标结果小的最大整数（向下取整）
print(3//2) # 结果是 1
print(-3/2) # 结果是 -2

# % 取余
print(6%2) # 结果是 0
# divmod(x,y) 函数 返回值为（x//y，x%y）
print(divmod(-3,2))  # (-2, 1)

# abs() 绝对值函数
y=-10
print(abs(y)) # 返回值为10

# int() 强制数据类型转换函数，强制转换为整数
print(int(1.1)) # 返回值为1
# float()                 强制转换为浮点数
print(float(1))  #返回值为1.0
# complex(re,img)         返回一个复数，re为实部，img为虚部
#c.conjugate()            返回c的共轭复数
# x**y 等价于 pow(x,y)
#pow(x,y,z) 等价于 x**y%z