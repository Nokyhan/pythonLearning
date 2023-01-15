import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 6, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()

# 9*9乘法口诀表
i: int = 1
j: int = 1
while i <= 9:
    while j <= 9:
        print(i, '*', j, '=', i * j, end="")
        j += 1
    i += 1
    print("")
