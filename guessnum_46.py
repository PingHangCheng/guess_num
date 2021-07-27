'''
一、產生一隨機整數1~100(不要印出來)
二、讓使用者重複輸入數字去猜
三、猜對的話印出"終於猜對了！"
四、猜錯的話，要告訴他比答案大/小
'''
import random
r = random.randint(1,100)
while True:
    num = int(input('請輸入一個數字來猜: '))
    if num > r:
        print('你輸入的數字比較大')
    elif num == r:
        print('終於猜對了！')
        break
    elif num < r:
        print('你輸入的數字比較小')
        