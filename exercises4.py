# ZYF-04-基础-爱因斯坦阶梯

# 编写一个程序，打印出0-100所有的奇数
# 我的代码
dig_list = range(1,101)
for dig in dig_list:
    if (dig + 1) % 2 == 0:
        print(dig)
    else:
        pass

# 老师的代码
ls = range(1,101)
for i in ls:
    if i % 2 == 1:
        print(i)