# ZYF-04-基础-爱因斯坦阶梯
# 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上两阶，剩余1阶。若每步上3阶，余2阶。若每步上5阶，余4阶梯。若每步上6阶，余5阶。若每步上7节，则一节不剩。
# 我的代码
ls = range(1,1000)
for i in ls:
    if (i % 2 == 1) and (i % 3 ==2) and (i % 5 == 4) and (i % 6 == 5) and (i % 7 == 0):
        print(i)
        #break
    else:
        pass

# 老师的代码
x = 0
while x < 1000:
    if (x % 2 == 1) and (x % 3 ==2) and (x % 5 == 4) and (x % 6 == 5) and (x % 7 == 0):
        print(x)
        x = x + 1
        #break
    else:
        x = x + 1
print('循环结束')