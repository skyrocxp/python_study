# LY-04-for
# 简单图形打印
'''
打印一下图形在输出上面
* * * * *
* * * * *
* * * * *
* * * * *
'''
print("* * * * *")
print("* * * * *")
print("* * * * *")
print("* * * * *")
print("------我-是-华-丽-的-分-割-线-------")

# 更改上面代码
print("* "* 5)
print("* "* 5)
print("* "* 5)
print("* "* 5)
print("------我-是-华-丽-的-分-割-线-------")

# 利用for循环更改上面案例
for i in range(1,5):
    print("* " * 5)
print("------我-是-华-丽-的-分-割-线-------")

# 利用双层for循环更改上面案例
for i in range(1,5):
    # 利用for循环打印一行星号
    for j in range(5):
        print("*",end = " ")
    # 换行
    print("")
print("------我-是-华-丽-的-分-割-线-------")

# 简单图形打印
'''
打印一下图形在输出上面
* * * * *
*       *
*       *
* * * * *
'''
'''
思路:
1. 正常利用for循环进行打印
2. 如果是第一行,或者最后一行,正常打印
3. 否则,判断打印列,如果是第一列或最后一列,打印星号,否则打印空格
'''
# 外层循环控制行
for i in range(4):
    if i == 0 or i == 3:
        print("* " * 5)
    else:
        for j in range(5):
            if j == 0 or j == 4:
                print("* ",end = "")
            else:
                print("  ",end = "")
        print()