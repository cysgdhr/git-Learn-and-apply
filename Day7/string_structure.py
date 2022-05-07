"""
显示走马灯的文字

Version: 0.01
Author: cy
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
