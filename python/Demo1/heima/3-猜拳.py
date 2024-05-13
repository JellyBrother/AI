'''
    定义变量
    使用变量
    看变量特点
'''
import random
player = int(input('请出拳：剪刀0，石头1，布2'))
computer = random.randint(0,2)
print(f'玩家是 {player}')
print(f'电脑是 {computer}')
if ((player==0) and (computer ==2)) or ((player==1) and (computer ==0)) or ((player==2) and (computer ==1)):
    print('玩家获胜')
elif ((player==0) and (computer ==0)) or ((player==1) and (computer ==1)) or ((player==2) and (computer ==2)):
    print('平局')
else:
    print('电脑赢')

# 三元表达式
result = player if player>computer else computer
print(f'结果是 {result}')