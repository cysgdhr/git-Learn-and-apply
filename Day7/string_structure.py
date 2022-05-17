"""
显示走马灯的文字

Version: 0.01
Author: cy
"""
"""
import os
import time

def main():
    content = '北京欢迎你为你开天辟地........'
    while True:
        os.system('cls') #清屏幕
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()
"""

"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
：param code_len: 验证码的长度(默认4个字符)
：return 由大小写英文字符和数字构成的随机验证码

Version: 0.01
Author: cy
"""
"""
import random
def generate_code(code_len = 4):

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

def main():
    print(generate_code(6))
if __name__ == '__main__':
    main()
"""

"""
设计一个函数返回给定文件的后缀名

Version: 0.01
Author: cy
"""
def suffix_get(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
def main():
    print(suffix_get('string_structure.py'))
if __name__ == '__main__':
    main()


