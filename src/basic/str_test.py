print("1：ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符") 
print(ord('A'), chr(65))
print(ord('a'), chr(97))
print(ord('中'), chr(20013))
print(ord('文'), chr(25991))

print("2：encode()方法可以把str转换为bytes，decode()方法可以把bytes转换为str")
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))  
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print("3：len()函数计算str的长度时，计算的是str的字符数，如果换成bytes，len()函数就计算字节数")
print(len('Hello, Python!'))
print(len('中文'))  # 计算字符数
print(len('中文'.encode('utf-8')))  # 计算字节数

print("4：%s和%d的区别，%s表示用字符串替换，%d表示用整数替换")
'hello %s' % 'world'
'Hi %s, you have %d $' % ('jane', 1000)

print('5: 格式化整数和浮点数还可以指定是否补0和整数与小数的位数')
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('6: str的format()方法也可以用来格式化字符串')
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)

print('7: f-string是Python 3.6引入的一种新的字符串格式化方法，使用起来非常方便')
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

print('8: 练习：计算提升的百分比')
s1 = 72
s2 = 85
res = ((s2 - s1) / s1) * 100
print(f'从 {s1} 提升到了 {s2}，提升了 {res:.1f}%')