# 什么是BIF？ Python3提供了多少个BIF

# BIF是内建函数，Python3提供了68个内建函数

# Tuling和tuling一样吗？

# 不一样，Python严格区分大小写

# 字符串的拼接
"我喜欢" + "韩雪雪" + "韩雪雪也喜欢我"

#编写程序，要求用户输入姓名，并且打印你好，姓名
name = input('请输入你的姓名：')
print ("你好，"+name)

# 编写程序，用户输入1-100之间的整数并判断，如果输入正确，打印，你好帅
# 如果输入错误，打印“丑八怪~~~求你别把灯打开”

# 我做出来的
num = int(input('请输入1-100之间的整数:'))
if 1 <= num <= 100:
    print("你好帅")
else:
    print('丑八怪~~~求你别把灯打开')

# 老师教的
temp = input('请输入1-100之间的整数：')
if temp.isdigit():
    temp = int(temp)
    if 1 <= temp <= 100:
        print('你好帅')
    else:
        print('你丑八怪~~~求你别把灯打开')
else:
    print('丑八怪~~~求你别把灯打开')
