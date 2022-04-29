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

num = int(input('请输入一个正整数：'))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
print('反转之后是%d' % reverse_num)

