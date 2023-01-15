# 字符串
x = "12321"
var = "是回文数" if x == x[::-1] else "不是回文数"
print(var)

# 常用函数
x = "I Love China!"
# capticalize() ,字符串首字母变成大写，其他字母变成小写
# caseflod()，返回所有字母都是小写的新字符串
# title(),每个单词的首字母大写
# swapcase(),大写变小写，小写变大写
# upper() ,所有字母变大写
# lower() 所有字母变小写（只能处理英语）

## 左中右对齐 第二个参数可以指定填充的字符
# center(nums_char) ,nums_char设置字符串总长度并居中对齐
# rjust() 右对齐
# ljust() 左对齐
# zflii() 用0填充

# 字符串查找功能
x = "上海自来水来自海上"
# count()计数
print(x.count("海"))
# fine() 找特定字符位置，默认左至右第一个，找不到返回—1
print(x.find("海"))
# 替换
# expandtabs()，将所有Tab变成空格（指定变成多少个） # 没有生效
code = """
    "Embrace your life!"
   "hhh" """
new_code = code.expandtabs(tabsize=3)
print(new_code)

# replace(old,new,-1) old->new -1表示所有替换
# translate() 根据表格内容进行替换，通常会与maketrans()函数搭配使用
table=str.maketrans("abcde","12345")
st="I love China!"
print(st.translate(table))

# startswith()，判断参数是否在起始位置，可以指定搜索起始和结束位置，参数可以为元组
x="他爱python"
if x.startswith(("你","我","他")):
    print("任何人都喜欢python")
# endswith(),判断是否在末尾位置
# istitle() 判断每个单词首字母是否是大写
# isupper() 是否是大写
# isspace() 是否是空白
# isdecimal() 检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
# isdigits() 检测字符串是否只由数字组成，只对 0 和 正数有效。
# isnumeric() 对于 Unicode 数字、全角数字（双字节）、罗马数字和汉字数字会返回 True ，其他会返回 False。
# isidentifier() 如果是有效标识符，则返回TRUE， 有效标识符：仅包含字母数字字母（a-z）和（0-9）或下划线（_）

## 截取字符串
# lstrip(m) 去除左侧匹配字符串，按照单个字符为单位，进行匹配去除
# rstrip() 去除右侧空白
# strip() 去除给定字符 ,只是头或尾，不影响中间字符
# removeprefix(s) 去除前缀的 字符串 s
# removesuffix(s) 去除后缀 的字符串s

## 拆分字符串
# partition(x) 以x为分隔符进行分割，返回一个三元组
# split(s)，以s为分隔符，对字符串进行切分
# splitlines() 按照换行符进行切分

## 字符串拼接
# join()
".".join(["www","nokyhan","com"])

## 格式化字符串 {}用于占位
year=2023
temp="今年是{}年"
print(temp.format(year))
#"{:^10}".format(520)

