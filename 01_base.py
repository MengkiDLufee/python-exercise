a = 1
print(a) # 1

a = 2
print(a) # 2

# 类型
a = 1
print(type(a)) # <class 'int'>
a = 12.3
print(type(a)) # <class 'float'>
a = True
print(type(a)) # <class 'bool'>
a = 'hello'
print(type(a)) # <class 'str'>
a = [1, 2, 3]
print(type(a)) # <class 'list'>
a = (1, 2, 3)
print(type(a)) # <class 'tuple'>
a = {1, 2, 3}
print(type(a)) # <class 'set'>
a = {'name': 'Tom', 'age': 18}
print(type(a)) # <class 'dict'>
a = None
print(type(a)) # <class 'NoneType'>


# 运算符

# 按位翻转, 一元加号和减号
print(~2) # -3
print(+2) # 2
print(-2) # -2

# 算数运算符
a = 10
b = 3
print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(a / b) # 3.3333333333333335
print(a // b) # 3
print(a % b) # 1
print(a ** b) # 1000

# 赋值运算符
a = 10
b = 3
a += b
print(a) # 13
a -= b
print(a) # 10
a *= b
print(a) # 30
a /= b
print(a) # 10.0
a //= b
print(a) # 3.0
a %= b
print(a) # 0.0
a **= b
print(a) # 0.0

# 比较运算符
a = 10
b = 3
c = '10'
print(a == b) # False
print(a == c) # False
print(a != b) # True
print(a > b) # True
print(a < b) # False
print(a >= b) # True
print(a <= b) # False

# 逻辑运算符
a = True
b = False
print(a and b) # False
print(a or b) # True
print(not a) # False

# 位运算符
a = 60 # 0011 1100

print(a & 13) # 12 # 0000 1100
print(a | 13) # 61 # 0011 1101
print(a ^ 13) # 49 # 0011 0001
print(~a) # -61 # 1100 0011
print(a << 2) # 240 # 1111 0000
print(a >> 2) # 15 # 0000 1111

# 成员运算符
a = [1, 2, 3]
print(1 in a) # True
print(4 in a) # False
print(1 not in a) # False
print(4 not in a) # True

# 身份运算符
a = 1
b = 1
print(a is b) # True
print(a is not b) # False
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # False
print(a is not b) # True

# 运算符优先级
# ** 指数 (最高优先级)
# ~ + - 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
# * / % // 乘, 除, 取模和取整除
# + - 加法减法
# >> << 右移, 左移运算符
# & 位 'AND'
# ^ | 位运算符
# <= < > >= 比较运算符
# <> == != 等于运算符
# = %= /= //= -= += *= **= 赋值运算符
# is is not 身份运算符
# in not in 成员运算符
# not or and 逻辑运算符


