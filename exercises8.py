# LY-05-for
# 简单图形打印
'''
打印一下图形在输出上面
*
* *
* * *
* * * *
* * * * *
'''
# 方案1
for i in range(1,6):
    print("* " * i)
print("------我-是-华-丽-的-分-割-线-------")

# 方案2
for i in range(1,6):
    # 打印一行
    # 每一行打印几个星号,跟行号相关
    # 一行内打印不需要换行,一行打印完毕换行
    for j in range(i):
        print("* ",end = "")
    print()
print("------我-是-华-丽-的-分-割-线-------")
'''
打印空心三角形
*
* *
*   *
*     *
* * * * *
'''
# 第一个方法,直接使用Print
# 第二个方法,使用for循环
for i in range(15):
    for j in range(i+1):
        if i == 14:
            print("* ",end = "")
        elif j == 0 or j == i:
            print("* ",end = "")
        else:
            print("  ",end = "")
    print()