"""
输入M和N计算C(M,N)

Version: 0.01
Authror: cy
"""
"""
M = int(input('请输入M：'))
N = int(input('请输入N：'))
fm = 1
for num in range(1, M + 1):
    fm *= num
fn = 1
for num in range(1, N + 1):
    fn *= num
fmn = 1
for num in range(1, M - N):
    fmn *= num
print(fm // fn // fmn)
"""

#用函数来计算
"""
def fac(num):
    result = 1
    for n in range(num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m - n))
"""

"""
实现计算最大公约数和最小公倍数的函数

Version: 0.01
Author: cy
"""
"""
def gcm(x, y):
#求最大公约数
    (x, y) = (y, x) if x > y else (x, y)
    for value in range(x, 0, -1):
        if x % value == 0 and y % value == 0:
            return value
"""
"""
    rem =  x % y
    while rem !=0:
        x = y
        y = rem
        rem = x % y
    return y
"""

"""
def lcm(x, y):
#求最小公倍数
    return x * y // gcm(x, y)
"""


"""
判断一个数是不是回文数

Version: 0.01
Author: cy
"""

"""
def is_palindrome(num):
#判断一个数是不是回文数
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
"""

"""
判断一个数是不是素数的函数

Version: 0.01
Author: cy
"""

def is_prime(num):
    for x in range(2, (num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True if num != 1 else False
