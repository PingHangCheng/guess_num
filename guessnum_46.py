'''
一、產生一隨機整數1~100(不要印出來)
二、讓使用者重複輸入數字去猜
三、猜對的話印出"終於猜對了！"
四、猜錯的話，要告訴他比答案大/小
五、延伸：讓使用者決定隨機數範圍
'''
import random
start = int(input('請決定隨機數字開始值： '))
end = int(input('請決定隨機數字結束值: '))
r = random.randint(start,end)
count = 0
while True:
    num = int(input('請輸入一個數字來猜: '))
    count += 1 # count = count + 1
    if num > r:
        print('你輸入的數字比較大')
    elif num == r:
        print('終於猜對了！' )
        print('這是你猜的第', count, '次')
        break
    elif num < r:
        print('你輸入的數字比較小')
    print('這是你猜的第', count, '次')
        