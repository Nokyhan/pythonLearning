# debug函数
print("Hello World!")
try:
    print(5/0)
except ZeroDivisionError:
    print("被除数不能是0")

# %% filename
filename="alice.txt"
try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except:
    pass
print("今天天气很好啊！")