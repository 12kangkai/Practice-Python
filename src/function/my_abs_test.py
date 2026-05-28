import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    """根据角度移动"""
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def mul(*parameters):
    """计算乘积"""
    if not parameters:
        raise ValueError("至少需要一个参数")
    product = 1
    for n in parameters:
        product *= n
    return product

print(mul(5))
print(mul(5, 6))
print(mul(5, 6, 7))

assert mul(5) == 5
assert mul(5, 6) == 30
assert mul(5, 6, 7) == 210

def move(n,a,b,c):
    """参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法"""
    if n == 1:
        print(f"{a} -> {c}")
    else:
        move(n-1, a, c, b)
        print(f"{a} -> {c}")
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')

