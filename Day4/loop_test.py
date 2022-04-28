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


