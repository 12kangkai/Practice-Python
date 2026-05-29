from collections.abc import Iterable

def findMinAndMax(L):

    if len(L) == 0:
        return (None, None)
    
    if not isinstance(L, Iterable):
        raise ValueError("输入必须是一个可迭代对象")
    
    min_value = max_value = L[0]
    for num in L:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num
    
    return (min_value, max_value)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')