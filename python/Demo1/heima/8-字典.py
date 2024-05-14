'''

'''
dict = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict)

print(dict.keys())

print(dict.values())

print(dict.items())

for key in dict.keys():
    print(key)

for item in dict.items():
    print(item)

for key, value in dict.items():
    print(f'key is {key} ,value is {value}')

s1 = {10, 20}
s1.add(100)
s1.add(10)
print(s1)

s1 = {10, 20}
# s1.update(100) # 报错
s1.update([100, 200])
s1.update('abc')
print(s1)

s1.remove(10)
s1.discard(10)
print(s1)

list1 = ['a', 'b', 'c']
for i in enumerate(list1):
 print(i)
for index, char in enumerate(list1, start=1):
 print(f'下标是{index}, 对应的字符是{char}')

