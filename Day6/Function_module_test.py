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
def fac(num):
    result = 1
    for n in range(num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m - n))