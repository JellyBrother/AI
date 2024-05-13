'''
    循环
'''
time = 0
while time < 5:
    print(f'打印次数 {time+1}')
    time+=1

# 0-100累加
i = 0
i1 = 0

while i<=100:
    i1 = i1 + i
    i+=1

print(i1)

# 0-100偶数相加
j = 0
j1 = 0

while j<=100:
    if (j % 2 == 0):
        j1 += j
    j+=1

print(j1)


# 0-100偶数相加
i = 0
i1 = 0

while i<=100:
    i1 = i1 + i
    i+=2

print(i1)



