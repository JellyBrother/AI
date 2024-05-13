# 单行注释
print("开始猜数字")
temp = input("请输入猜测的数字")
guess = int(temp)
'''
    多行注释
'''
if guess == 8:
    print(f"恭喜你猜对了 {guess}")
elif guess == 9:
    print('你很棒棒')
else:
    print(f"很遗憾，你猜错了 {guess}")
print("游戏结束")