### 元组
rythe = (1, 2, 3, 4, 5, '上山大老鼠')
print(rythe)

# 元组可以通过下标访问，只能查询，不能修改，无元组推导式
# 生成一个只有一个元素的元组要加逗号 （生成元组亦可称为打包）
x=(520,)
# 解包，将序列的各个元素赋值给不同的变量
## attention 赋值左边的变量数目必须要和元组数目一致
x,y,z,m,n,z=rythe

# 多重赋值的实质是元组的打包与解包
# 元组中的元素若是指向可变列表，则仍可以修改元组内容
