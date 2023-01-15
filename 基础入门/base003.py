# 布尔类型 非空为TRUE 空为FALSE
bool(250)  # 返回值为TRUE
bool(0)  # 返回结果为FALSE

if 520 > 250:
    print("TRUE")

# 逻辑运算符 and or not 或且非
# and需要运算完，or有真则输出
# 从左到右，只有当第一个操作数的值无法确定逻辑运算的结果时，才对第二个操作数进行求值
var = (not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9)
print(var)

# 运算符优先级
# 运算优先计算优先级高的 not > and > or
