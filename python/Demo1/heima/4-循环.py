'''
    循环
'''
time = 0
while time < 5:
    print(f'打印次数 {time + 1}')
    time += 1

# 0-100累加
i = 0
i1 = 0

while i <= 100:
    i1 = i1 + i
    i += 1

print(i1)

# 0-100偶数相加
j = 0
j1 = 0

while j <= 100:
    if (j % 2 == 0):
        j1 += j
    j += 1

print(j1)

# 0-100偶数相加
i = 0
i1 = 0

while i <= 100:
    i1 = i1 + i
    i += 2

print(i1)

i = 0

while i < 6:
    i += 1
    if i == 4:
        print('苹果吃抱了')
        break
    if i == 2:
        print('这个苹果有虫子')
        continue
    print(f'第几个苹果{i}')
print('结束')

i = 0
while i < 3:
    i += 1
    j = 0
    while j < 3:
        j += 1
        print('洗碗')

    print('拖地')
print('结束')

i = 0
while i < 9:
    i += 1
    j = 0
    while j < 9:
        j += 1
        print('*', end='')
    print()
print('结束')

i = 0
while i < 9:
    j = i
    while j >= 0:
        j -= 1
        print('*', end='')
    i += 1
    print()
print('结束')

# 9*9乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        n = i * j
        m = '  '
        # if n > 9:
        #    m = '  '
        if ((i == 3) and (j == 2)) or ((i == 4) and (j == 2)):
            m = '   '
        print(f'{j} * {i} = {n}' + m, end='')
        j += 1
    i += 1
    print()
print('结束')

# 9*9乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f'{j} * {i} = {i * j}', end='\t')
        j += 1
    i += 1
    print()
print('结束')

str = 'itheima'
for i in str:
    print(i)
print('结束')

str = 'itheima'
for i in str:
    if i == 'm':
        break
    if i == 'e':
        continue
    print(i)
print('结束')

str = 'itheima'
for i in str:
    print(i)
else:
    print('循环结束')

str = 'itheima'
for i in str:
    if i == 'm':
        break
    if i == 'e':
        continue
    print(i)
else:
    print('循环结束')
print('结束')

time = 0
while time < 5:
    print(f'打印次数 {time + 1}')
    time += 1
else:
    print('循环结束')

time = 0
while time < 5:
    time += 1
    if time == 3:
        continue
    print(f'打印次数 {time + 1}')
else:
    print('循环结束')

time = 0
while time < 5:
    time += 1
    if time == 4:
        continue
    print(f'打印次数 {time + 1}')
    time += 1
else:
    print('循环结束')




