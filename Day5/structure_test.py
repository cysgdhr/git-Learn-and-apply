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

