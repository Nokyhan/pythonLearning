# %% 文件操作
a = "星垂平野阔，月涌大江流"
print(a.encode())  # 输出a的编码
# %% 2
f = open("f.txt", 'w')
# w 覆盖写模式，文件不存在则创建，存在则完全覆盖
# r 只读模式，默认值，如果文件不存在，返回FileNotFoundError
# a 追加写模式，不存在则创建，存在则在最后追加内容
f.writelines(a)
f.close()

# %% 3
tf = open("f.txt", "rt")
print(tf.readline())  # 读取一行
tf.close()

# %% 4
bf = open("f.txt", "rb")  # windows存储中文使用gbk编码
print(bf.readline())
bf.close()

# %% 文件操作
# <变量名>=open(<文件名>,<打开方式>)
# readline() 读取某行
# readlines() 读入所有行，以每行形成列表

# %% 词频统计
# 借助词库，确定字符间的关联概率
import jieba as jb

a = "中华人民共和国在1949年10月1日成立了！"
print("无冗余切分：", jb.lcut(a))
print("全模式切分：", jb.lcut(a, cut_all=True))  # 包含各种可能情况
print("搜索引擎模式：", jb.lcut_for_search(a))

# %%
import jieba
import wordcloud
txt = open(r"C:\Users\Noky-han\PycharmProjects\pythonLearning\基础入门\背景.txt", encoding="utf-8").read()
# 加载停用仓库
stopwords = [line.strip() for line in open(r"C:\Users\Noky-han\PycharmProjects\pythonLearning\基础入门\停用词库.txt", encoding="utf-8").readlines()]
# 切分文档
words=jieba.lcut(txt)
counts={}
for word in words:
    # 排除在停用词表中的词
    if word not in stopwords:
        if len(word)==1:
            continue
        else:
            # 使用字典 （键 为 词名 值为 次数）
            counts[word]=counts.get(word,0)+1
items=list(counts.items())      #字典转换成列表，并按照
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
# key=lambda x:x[k] 按照元组中第k+1个元素进行排序
items.sort(key=lambda x:x[1],reverse=True)
for i in range(30):
    word,count =items[i]
    print("{:<10}{:>7}".format(word,count))
# 创建一个词云对象
w=wordcloud.WordCloud(width=1000,height=700,font_path=r"C:\Users\Noky-han\PycharmProjects\pythonLearning\基础入门\STXINWEI.TTF")
w.generate("".join(txt.replace(" ","").replace("\n","")))

w.to_file("cloud.png")

# %% 词云测试
import wordcloud
word_c=wordcloud.WordCloud()

word_c.generate("Hello World!")
word_c.to_file("py.png")
