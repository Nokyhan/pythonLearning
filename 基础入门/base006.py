# 列表
import copy

lis = [1, 2, 3, 4, 5, 'NOKY']
for each in lis:
    print(each)

# 列表可以使用下表进行索引,列表存储是从 0 开始
print(lis[3])  # 访问的是第 4 个元素
# len()函数，获取参数的长度
print(lis[len(lis) - 1])  # 输出倒数第一个元素
print(lis[-1])  # 和上面等同

# 切片
print(lis[2:])  # 从2开始到最后的列表
print(lis[::-1])  # 倒序输出，和matlab很像

# 向列表，添加元素 append()函数
heros = ['钢铁侠', '绿巨人']
heros.append('黑寡妇')
print(heros)
# 可以使用切片,相当于对特定位置赋值
heros[len(heros):] = ['HHH']
print(heros)
# insert(loc,elem)命令，在特定元素位置 列表的第loc位置 插入 元素 elem
# e.g. 在列表最后插入数据
heros.insert(len(heros), 'han')

# 删除指定元素 remove()方法
heros.remove('HHH')

# 弹出指定位置元素，并输出 pop()方法
heros.pop(len(heros) - 1)

# 一次性清除所有元素 clear()方法
heros.clear()  # 最后输出为空列表
# sort() 排序函数
# reverse() 顺序翻转
# index() 获取指定元素索引值 是从1开始的
list_h = ['A', 'C', 'D', 'B']
# 默认从小到大排列
list_h.sort()
print(list_h)

# 浅拷贝,list_h所有元素
copy_2 = list_h[:]
print(copy_2)

## 创建二位列表
matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出第一行第一元素
print(matrix_2[0][0])

# 通过循环语句创建列表 *只是对列表引用的copy
A = ['0', '0', '0']
for i in range(3):
    A[i] = [0] * 3
print(A)
import copy

# 浅拷贝，拷贝变量引用
# 深拷贝，拷贝变量值
matrix_2_copy = copy.copy(matrix_2)
matrix_2_deepcopy = copy.deepcopy(matrix_2)
matrix_2_copy[0][1] = 10
print(matrix_2_copy)
print(matrix_2)
print(matrix_2_deepcopy)

# 列表推导式
## expression for target in list [condition]
AAA = [1, 2, 3, 4, 5]
AAA = [i * 2 for i in AAA]
print(AAA)

# 将字符串转换为Unicode编码并存储起来 ord() 函数
code = [ord(c) for c in 'NOKY']
print(code)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_1 = [matrix[i][2 - i] for i in range(len(matrix))]
print(matrix_1)
AA=[]
for row in matrix:
    for col in row:
        AA.append(col)
print(AA)
# 等价于
AAAA=[col for row in matrix for col in row]
print(AAAA)

## 列表推导式 和 循环 一循环为逐个修改 ；列表推导式 创建一个新的列表

### 创建多维列表
S=[[0]*3 for i in range(3)]

words = ['Great','FishC','Brilliant','Excellent','Fantastic']
word=[c for c in words if c[0]=='F']

