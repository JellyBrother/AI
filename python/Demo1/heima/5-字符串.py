'''
    定义
    类型
    选取 字符串[开始位置0:结束位置最后:步长1]
    查找 .find(要查找的字符串,查找开始位置,查找结束位置)
    修改 .replace(旧字符串,新字符串,替换次数)
'''
my_name = 'I\'m TOM'
print(type(my_name))
my_name = "TOM"
print(type(my_name))
'''
支持回车换行，并且不添加其他字符
'''
my_name = '''TOM'''
print(type(my_name))
print(f'name\'s{my_name}')
print(type(my_name))

print(f'name\'s{my_name}')
print('name is %s' % my_name)
print(f'name\'s{my_name[2]}')

# str = input('请输入')
# print(str)
# print(type(str))

# 序列名[开始位置0:结束位置最后:步长1]
my_name = '''0123456789'''
print(f'name {my_name[2:9:1]}')  # 2345678
print(f'name {my_name[2:9:3]}')  # 258
print(f'name {my_name[2:9]}')  # 2345678
print(f'name {my_name[:9]}')  # 012345678
print(f'name {my_name[2:]}')  # 23456789
print(f'name {my_name[:]}')  # 0123456789

print(f'name {my_name[::-1]}')  # 9876543210
print(f'name {my_name[-9:-2]}')  # 1234567
print(f'name {my_name[-5:-2:-1]}')  # 选取反向和步长反向冲突，选不出来
print(f'name {my_name[-2:-5:-1]}')  # 876
print(f'name {my_name[-9:-2:2]}')  # 1357

# 查找 .find[要查找的字符串:查找开始位置:查找结束位置]

my_name = '   hello world and qwert and asdfg and python   '
print(my_name.find('ands'))  # -1
print(my_name.find('and'))  # 12
print(my_name.find('and', 13, 30))  # 22

# print(my_name.index('ands'))  # 报错不往下执行
print(my_name.index('and'))  # 12
print(my_name.index('and', 13, 30))  # 22

print(my_name.count('ands'))  # 0
print(my_name.count('and'))  # 3
print(my_name.count('and', 13, 30))  # 1

print(my_name.rfind('and'))  # 32 从右开始查找

print(my_name.rindex('and'))  # 32 从右开始查找

print(my_name.replace('and', '456'))
print(my_name.replace('and', '456', 1))

print(my_name.split('and'))
print(my_name.split('and', 2))

mylist = ['hello world ', ' qwert ', ' asdfg ', ' python']
print('**456**'.join(mylist))

print(my_name.capitalize())  # 第一个字符大小
print(my_name.title())  #
print(my_name.upper())  #
print(my_name.lower())  #

print(my_name.lstrip())  #
print(my_name.rstrip())  #
print(my_name.strip())  #

my_name='hello'
print(my_name.ljust(10, '.'))  #
print(my_name.rjust(10, '.'))  #
print(my_name.center(10, '.'))  #

print(my_name.startswith('.'))  #
print(my_name.endswith('.'))  #

print(my_name.isalpha())  # 全是字母
print(my_name.isdigit())  # 全是数字
print(my_name.isalnum())  #
print(my_name.isspace())  # 全是空格