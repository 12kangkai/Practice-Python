def trim(s):
    start = 0
    end = len(s) - 1

    while start <= end and s[start] == ' ':
        start += 1

    while end >= start and s[end] == ' ':
        end -= 1

    return s[start:end + 1]
    

    

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')