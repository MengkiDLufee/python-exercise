def fac(num):
    res = 1
    for n in range(1, num + 1):
        res *= n
    return res

m = int(input('请输入一个整数：'))
print(fac(m)) 


