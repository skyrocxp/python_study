# ZYF-基础-运算符
# 1.这行代码什么意思：
# if not (money < 100)
# not意思为取反，等价于money >= 100

# 2.假设x = 1,y = 2,z = 3如何快速将三个变量交换
x,y,z = 1,2,3
print(x,y,z)
x,y,z = z,y,x
print(x,y,z)

# 3.成员资格运算符 in的用法
ls = range(100)
if 100 in ls:
    print(True)
else:
    print(False)

ls = range(100)
if not 100 in ls:
    print(True)
else:
    print(False)

# 4.range函数
ls = range(0,10,2)
for i in ls:
    print(i)

# 5.目测以下程序会打印什么
while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)
# 2 3

# 6.从代码效率方面考虑，以下代码有什么问题，如何改进
#i = 0
#string = 'ILovexue'
#while i < len(string):
#    print(i)
#    i += 1

i = 0
string = 'ILovexue'
leng = len(string)
while i < leng:
    print(i)
    i += 1

# 设计一个用户密码验证程序，用户有三次机会验证密码是否正确。
# 如果用户输入的内容包括“*”的话，则不计算在内

key = 'password'
times = 3
while times:
    input_key = input('请输入密码：')
    if input_key == key:
        print('验证通过')
        break
    elif '*' in input_key:
        print('密码不包括“*”号')
    else:
        times = times - 1
        print('输入错误')