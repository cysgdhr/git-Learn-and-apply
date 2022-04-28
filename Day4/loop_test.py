"""
用for循环实现1~100求和

Version: 0.01
Author: cy
"""
"""
#for....in....
sum = 0
for x in range(101):
    sum += x
print('1~100的和是%d' % sum)
"""
"""
#while....
sum = 0
x = 0
while x < 100 :
    x += 1
    sum += x
print('1~100的和是%d' % sum)
"""


"""
用for循环实现1~100之间的偶数求和

Version: 0.01
Author: cy
"""

"""
#for...in....
sum = 0
for x in range(0, 101, 2):
    sum += x
print('0~100的偶数和为 %d' % sum)
"""
"""
#while....
sum = 0
x = 0
while x < 100 :
    x += 2
    sum += x
print('0~100的偶数和为 %d' % sum)
"""
"""
猜数字游戏

Version: 0.01
Author: cy
"""
"""
import random

Answer = random.randint(1, 100)
Guess = 0
Frequency = 0
while Guess != Answer:
    Guess = int(input('请输入一个1~100的数字：'))
    Frequency += 1
    if Guess > Answer:
        print('小一点')
    elif Guess == Answer:
        print('猜对了，一共猜了%d次' % Frequency)
    else:
        print('大一点')
"""

"""
#有break
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了')
        break
print('你总共猜了%d次' % counter)
"""

"""
输出乘法表口诀表

Version: 0.01
Author: cy
"""
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (i, j, i * j), end = '\t')
    print()
"""

"""
输入一个正整数判断它是不是素数

Version: 0.01
Author: cy
"""
"""
from math import sqrt

num = int(input('请输入一个正整数：'))
root = int(sqrt(num))
print('root = %d' % root)
judge = True
for x in range(2, root + 1):
    if num % x == 0:
        judge = False
        break      
if judge and num != 1:
    print ('%d是素数' % num)
else:
    print('%d不是素数' % num)
"""

"""
输入两个正整数计算他们的最大公约数和最小公倍数

Version: 0.01
Author: cy
"""

"""
x = int(input('请输入第一个正整数：'))
y = int(input('请输入第二个正整数：'))

divisor = 0
multiple = x * y
remainder = x % y
print('remainder %d' % remainder)
while remainder != 0:
    x = y
    y = remainder
    remainder = x % y
divisor = y
multiple = multiple // divisor
print('最小公倍数是%d' % multiple)
print('最大公约数是%d' % divisor)
"""

"""
x = int(input('请输入第一个正整数：'))
y = int(input('请输入第二个正整数：'))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('整数%d和整数%d的最大公约数是%d' % (x, y, factor))
        print('整数%d和整数%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
"""
