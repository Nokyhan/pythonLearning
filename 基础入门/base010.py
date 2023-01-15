import turtle as t

t.title("小风车")
# 设置画线颜色，和图形的填充颜色
t.color("black","pink")
for i in range(10):
    t.speed(10)
    t.begin_fill()
    t.pendown()
    t.seth(45+36*i)
    t.forward(100)
    t.seth(45+36*i+90)
    t.forward(80)
    t.goto(0, 0)
    t.end_fill()
t.stamp()

t.done()
