"""
输入年份判断是不是闰年

Version: 0.01
Author: cy
"""
year = int(input('请输入年份：'))
is_leap = ((year % 4 == 0 and  year % 100 != 0) or year % 400)
print(is_leap)



"""
输入半径计算圆的周长和面积

Version: 0.01
Author: cy
"""
"""
r = float(input('请输入圆的半径：'))
C = 3.1416 * r * 2
S = 3.1416 * r * r
input('半径为%.2f 的周长为%.2f，面积为%.2f' % (r, C, S))
"""


"""
华氏温度转换为聂氏温度

Version: 0.01
Author: cy
"""
"""
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f聂氏度' % (f, c))
"""


"""
比较运算符和逻辑运算符的使用

Version: 0.01
Author: cy
"""
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not(1 != 2)
print('flag0 =', flag0)
print('flag1 =', flag1)
print('flag2 =', flag2)
print('flag3 =', flag3)
print('flag4 =', flag4)
print('flag5 =', flag5)
"""

#运算符练习
"""
赋值运算符和符合赋值运算符

Version: 0.01
Author: cy
"""

"""
a = 10
b = 3
a += b
a *= a + 2
print(a)
"""


#通过键盘输入整数实现运算
"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

Version: 0.1
Author: cy
"""
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
"""


#数据类型
"""
使用 type()检查变量的类型

Version: 0.1
Author: cy
"""
"""
a = 100
b = 13.14
c = 1 + 5j
d = "hello world"
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
"""


# 简单运算
"""
使用变量保存数据并进行加减乘除运算

Version: 0.1
Author: cy
"""
"""
a = 321
b = 12
print(a + b)
print(a - b)
print(a * b)
print(a / b)
"""