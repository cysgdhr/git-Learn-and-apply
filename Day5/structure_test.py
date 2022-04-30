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
for Rooster in range(20):
    for Hen in range(33):
        Chick = 100 - Rooster - Hen
        if 5 * Rooster + 3 * Hen + Chick / 3 == 100:
            print('公鸡%d只，母鸡%d只，小鸡%d只' % (Rooster, Hen, Chick))
