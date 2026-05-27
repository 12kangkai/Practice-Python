print('''line1
line2
line3''')

print("----------------")

print(r'''hello,\n
world''')

print("----------------")

a = 1
t_007 = '007'
result = True
print('a = %d, t_007 = %s, result = %s' % (a, t_007, result))

print("----------------")

a = t_007
t_007 = result
result = 1
print('a = %s, t_007 = %s, result = %d' % (a, t_007, result))

print("----------------")

x = 'abc'
y = x
x = 'def'
print('x = %s, y = %s' % (x, y))

print("----------------")

n = 123
f = 456.789
s1 = 'hello, world'
s2 = 'hello, \'Adam\''
s3 = r'hello, "Bart"'
s4 = r'''hello,
Lisa!'''
print(n, f, s1, s2, s3, s4)



