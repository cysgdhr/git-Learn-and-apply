"""
找出所有水仙花数

Version: 0.01
Author: cy
"""
"""
for num in range(100, 1000):
    a = num % 10
    b = num // 10 % 10
    c = num // 100
    if a ** 3 + b ** 3 + c ** 3 == num:
        print(num)
"""


"""
正整数的反转

Version: 0.01
Author: cy
"""
"""
num = int(input('请输入一个正整数：'))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
print('反转之后是%d' % reverse_num)
"""

"""
(https://baike.baidu.com/item/%E5%BC%A0%E4%B8%98%E5%BB%BA/10246238)
百钱百鸡问题

Version: 0.01
Author: cy
"""
"""
for Rooster in range(20):
    for Hen in range(33):
        for Chick in range(300):
            if(Rooster * 5 + Hen * 3 + Chick / 3 == 100) and (Rooster + Hen + Chick == 100):
                print("公鸡%d只，母鸡%d只，小鸡%d只" % (Rooster, Hen, Chick))
"""
"""
for Rooster in range(20):
    for Hen in range(33):
        Chick = 100 - Rooster - Hen
        if 5 * Rooster + 3 * Hen + Chick / 3 == 100:
            print('公鸡%d只，母鸡%d只，小鸡%d只' % (Rooster, Hen, Chick))
"""

"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌

Version: 0.01
Author: cy
"""
"""
from random import randint

Principal = 1000
Frequency = 1
while Principal != 0:
    if Frequency == 1:
        Bet = int(input("请下注："))
        while Bet > Principal:
            print("你的本金剩%d" % Principal)
            Bet = int(input("请重新下注："))

    Dice1 = randint(1, 6)
    Dice2 = randint(1, 6)
    Num = Dice1 + Dice2
    if Frequency == 1:
        if Num == 7 or Num == 11:
            print('骰子1是%d点，骰子2是%d点，总和%d，玩家胜' % (Dice1, Dice2, Num))
            Principal += Bet
        elif Num == 2 or Num == 3 or Num == 12:
            print('骰子1是%d点，骰子2是%d点，总和%d，庄家胜' % (Dice1, Dice2, Num))
            Principal -= Bet
        else:
            print('骰子1是%d点，骰子2是%d点，总和%d，没有赢家，继续摇' % (Dice1, Dice2, Num))
            Frequency += 1
            First_num = Num
    else:
        if Num == First_num:
            print('骰子总和是%d，和第一次骰子总和一样，玩家胜' % Num)
            Principal += Bet
            Frequency = 1
        elif Num == 7:
            print('骰子总和是7，庄家胜')
            Principal -= Bet
            Frequency = 1
print('你输光了')
"""

"""
#答案
from random import randint
money = 1000
while money > 0:
    print('你的总资产为：', money)
    needs_gon_on = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
print('你破产了，游戏结束!')
"""

"""
生成**斐波那契数列**的前20个数。

Version: 0.01
Author: cy
"""
"""
Number1 = 1
Number2 = 1
print('开始生成斐波那契数列：')
for Fre in range(0, 20):
    if Fre >= 2:
        print('%d' % (Number1 + Number2), end=' ')
        Number3 = Number1 + Number2
        Number1 = Number2
        Number2 = Number3
    else:
        print('%d' % Number1, end=' ')
"""
"""
a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')
"""


"""
找出1000以内的完美数

Version: 0.01
Author: cy
"""

"""
from math import sqrt

Sum = 0
for Num in range(2, 10000):
    for x in range(1, int(sqrt(Num)) + 1):
        if Num % x == 0:
            Sum += x
            if x != 1 and Num // x != x:
                Sum += Num // x
    if Num == Sum:
        print(Num, end=' ')
    Sum = 0
"""

"""
#答案
import math

for num in range(2, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)
"""

"""
输出100以内所有的素数

Version: 0.01
Author: cy
"""

import math

for num in range(2, 100):
    prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0 and factor != num:
            prime = False
            break
    if prime == True:
        print(num)
