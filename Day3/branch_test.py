"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Version: 0.01
Author: cy
"""

a = float(input('请输入边长a：'))
b = float(input('请输入边长b：'))
c = float(input('请输入边长c：'))
if a + b > c and a + c > b and b + c > a:
    print('三边长分别为%.1f，%.1f，%.1f可以构成三角形' % (a, b, c))
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('周长为 %.1f' % (a + b + c))
    print('面积为 %.1f' % s)
else:
    print('不能构成三角形')


"""
百分制成绩转换为等级制成绩
**要求**：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）
输出C；60分-70分（不含70分）输出D；60分以下输出E。

Version: 0.01
Author: cy
"""
"""
score = float(input('请输入成绩：'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('成绩%.1f分的等级是:' % score, grade)
"""

"""
英制单位英寸和公制单位厘米互换

Version: 0.01
Author: cy
"""
"""
Lenght_unit = input('请输入长度单位：')
Lenght = float(input('请输入长度：'))
if Lenght_unit == '厘米' or Lenght_unit == 'cm':
    print('%.2f厘米等于%.2f英寸' % (Lenght, Lenght / 2.54))
elif Lenght_unit == '英寸' or Lenght_unit == 'in':
    print('%.2f英寸等于%.2f厘米' % (Lenght, Lenght * 2.54))
else:
    print('长度单位输入错误，请输入有效单位')
"""


"""
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.01
Author: cy
"""
"""
x = float(input('请输入x的数值：'))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x +2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
"""
#另一种写法
"""
x = float(input('请输入x的数值：'))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
"""


""""
用户身份证明

Version: 0.01
Author: cy
"""
"""
username = input('请输入你的用户名：')
password = input('请输入你的账户密码：')
#如果账户名为cy，密码为147258，则验证成功，否则验证失败
if username == 'cy' and password == '147258':
    print('验证成功')
else:
    print('验证失败')
"""