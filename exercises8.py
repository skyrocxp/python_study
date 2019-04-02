# LY-05-for
# 简单图形打印
'''
打印以下图形在输出上面
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
for i in range(5):
    for j in range(i+1):
        if i == 4:
            print("* ",end = "")
        elif j == 0 or j == i:
            print("* ",end = "")
        else:
            print("  ",end = "")
    print()
print("------我-是-华-丽-的-分-割-线-------")

'''
打印以下图形在输出上面

* * * * *
* * * *
* * *
* *
*
'''
# i-for控制行号
# j-for控制列号
for i in range(5):
    for j in range(5-i):
        print("* ",end="")
    print()
print("------我-是-华-丽-的-分-割-线-------")

# i-for控制行号
# j-for控制列号
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("* ",end="")
    print()
print("------我-是-华-丽-的-分-割-线-------")

'''
打印空三角

* * * * *
*     *
*   *
* *
*
'''
for i in range(5):
    for j in range(5-i):
        if i == 0:
            print("* ",end = "")
        elif j == 0 or j == 5-i-1:
            print("* ",end = "")
        else:
            print("  ",end = "")
    print()
print("------我-是-华-丽-的-分-割-线-------")
'''
打印三角形,正三角形

    *
   * *
  * * *
 * * * *
* * * * *
'''
for i in range(1,6):
    # 总体思路是,先打印一行空格,代表星星前的空格
    # 再不换行,打印星号
    for j in range(6-i):
        print(" ",end = "")
    for k in range(i):
        print("* ",end = "")
    print()
print("------我-是-华-丽-的-分-割-线-------")
'''
打印空正三角形

    *
   * *
  *   *
 *     *
* * * * *
'''
for i in range(1,6):
    # 先打印第一行和最后一行,第一行为(6-i)个空格+"*"
    # 最后一行为5个("*"+空格)
    if i == 1:
        print(" "*(6-i)+"*")
    elif i == 5:
        print(" "+"* "* 5)
    # 打印中间部分,依然先打印空格

    else:
        for j in range(4-i):
            print(" ", end = "")
        # 空格后面第一个符号打印"*"+空格
        # 第行号个字符打印"*"+空格

        for k in range(i+1):
            if k == 1 or k == i:
                print("* ",end = "")
            # 其他地方用双空格补齐
            else:
                print("  ",end = "")
        print()
print("------我-是-华-丽-的-分-割-线-------")
