# numpy
import time

import numpy as np

my_arr = np.arange(1000000)
my_list = list(range(1000000))
# 设置起始时间
start = time.time()
for _ in range(10):
    my_arr = my_arr * 2
# 设置终止时间
end = time.time()
# 输出耗时总长
print("numpy耗时", end - start)

# 设置起始时间
start = time.time()
for _ in range(10):
    my_list2 = 2 * my_list
# 设置终止时间
end = time.time()
# 输出耗时总长
print("python耗时", end - start)

# %%
import numpy as np

list1 = [1.0, 2.0, 3.0, 4.0, 5.0]
list2 = list1.copy()
a = np.array([list1,list2])
print(a)
print("矩阵维度：",a.ndim)
print("矩阵大小：",a.shape)
print("（每列）最大值：",a.max(0))
print("（每行）最大值",a.max(1))
# %%
import numpy as np
list1=[1.1,2.2,3.3]
b=np.array(list1,dtype=np.string_)
print(b)
b1=b.astype(float)
print(b1.dtype)

#%% 切片与索引（高级）
# 布尔索引，筛选出满足表达式的项
# 序列索引，按照数组下标索引
#　花式索引 np.ix_方法，对输入的数组进行笛卡尔乘积，产生生成的索引下标

# %% 数组文件的输入和输出
import numpy as np
# arr=np.arange(10)
# np.save("arr",arr) np.savetxt()文件保存为字符串
# 载入保存的数组
a=np.load(r"C:\Users\Noky-han\PycharmProjects\pythonLearning\基础入门\arr.npy")

# %% 数组计算（数组广播）

import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=np.array([3,4,5])
c=a1+a2
print(c)
