# ZYF-03-基础-猜字游戏
# 10 < cost < 50的等价表达式
cost = 40
(10 < cost) and (cost < 50)

# 使用int()将小数转换成整数，结果是向上取整还是向下取整
print (int(3.6))

# 写一个程序，判断给定年份是否为闰年
# 闰年，能被4整除的年份

# 我的代码
year = int(input('请输入一个年份'))
if year % 4 == 0:
    print('该年为闰年')
else:
    print('该年不是闰年')

# 老师的代码
year = input('请输入一个年份')
if year.isdigit():
    year = int(year)

    if year % 4 == 0:
        print(str(year)+'年是闰年')
    else:
        print(str(year)+'年不是闰年')
else:
    print('请输入阿拉伯数字')


# 给用户三次机会，猜想我们程序生成的一个数字A，每次用户猜想提示用户大于还是小于A，三次机会后提示用户已经输掉了游戏

# 我的代码
import random
a = random.randint(1,10)
b = int(input('请输入一个1到10的数字:'))
if int(a) == int(b):
    print('你好棒，答对啦！')
    exit()
if int(b) > int(a):
    print('高了，再输入一次吧')
if int(b) < int(a):
    print('低了，再输入一次吧')
c = int(input())
if int(a) == int(c):
    print('你好棒，答对啦！')
    exit()
if int(c) > int(a):
    print('高了，再输入一次吧')
if int(c) < int(a):
    print('低了，再输入一次吧')
d = int(input())
if int(a) == int(d):
    print('你好棒，答对啦！')
    exit()
if int(d) > int(a):
    print('游戏结束，你输啦,答案是'+str(a))
if int(d) < int(a):
    print('游戏结束，你输啦，答案是'+str(a))

# 老师的代码
import random

secret = random.randint(1,100)

times = 3 #初始化用户的次数是3次

while times:
    num = input('请输入一个1到100的数字：')
    if num.isdigit():
        tmp = int(num)
        if tmp == secret:
            print('你好棒，答对啦！')
            break
        elif tmp < secret:
            print('你的数字太小了！')
            times = times - 1
        else:
            print('你的数字太大了！')
            times = times - 1
    else:
        print('叫你输入数字')

print('你的机会用完了！')