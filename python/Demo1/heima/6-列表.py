'''

'''
name_list = ['hello', 'world', 'qwert']
print(name_list)
print(name_list[1])

print(name_list.index('world'))
print(name_list.index('world', 0, 2))

print(name_list.count('world'))

print(len(name_list))

print('world' in name_list)
print('worlds' in name_list)

print('world' not in name_list)

name_list.append('12')
name_list.append(['12', '123'])
print(name_list)

name_list.extend("45")
name_list.extend(['12', '123'])

name_list.insert(2, "78")
print(name_list)

# del(name_list)
del (name_list[0])
print(name_list)

pop = name_list.pop()
print(pop)
print(name_list)

name_list.remove('4')
print(name_list)

# name_list.clear()
# print(name_list)

name_list[0] = 'asd'
print(name_list)

name_list.reverse()
print(name_list)

list = [9, 6, 5, 1, 7]
list.sort()
print(list)

list.sort(reverse=True)
print(list)

copy = list.copy()
print(copy)

i = 0
while i < len(copy):
    print(copy[i])
    i += 1
print('循环结束')

for i in copy:
    print(i)
print('循环结束')

list = [['11', '12', '13'], ['21', '22', '23'], ['31', '32', '33']]
for i in list:
    for j in i:
        print(j)
print('循环结束')

import random

teachers = ['1', '2', '3', '4', '5', '6', '7', '8']
office = [[], [], []]
for i in teachers:
    num = random.randint(0, 2)
    office[num].append(i)
print(office)

for i in office:
    print(f"长度 {len(i)}")
