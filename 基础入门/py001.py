# 将数据输出到文件中， 路径需存在
fp = open('D:/text.txt', 'a+')  # 不存在就创建，存在就追加(运行依次，追加一条)
print('HelloWorld', file=fp)
fp.close()

# 数据输出到一行
print('Hello', 'python')

######### 转义字符  ##########
#\n 表示换行
print('hello\nworld')
#\t 表示 空格
print('hello\tworld')
print('hellooo\tworld')