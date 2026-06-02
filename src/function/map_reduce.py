# map 和 reduce 教学代码

# ===== map 函数 =====
# map 对列表中的每个元素应用一个函数

# 例子 1: 将列表中的每个数字乘以 2
numbers = [1, 2, 3, 4, 5]

def double(x):
    return x * 2

result = list(map(double, numbers))
print("map 例子 1 - 乘以 2:")
print(f"原列表: {numbers}")
print(f"结果: {result}")
print()

# 例子 2: 将列表中的字符串转换为大写
words = ["hello", "world", "python"]

def to_upper(word):
    return word.upper()

result = list(map(to_upper, words))
print("map 例子 2 - 转换为大写:")
print(f"原列表: {words}")
print(f"结果: {result}")
print()

# 例子 3: 将字符串转换为整数
string_numbers = ["1", "2", "3", "4", "5"]
result = list(map(int, string_numbers))
print("map 例子 3 - 字符串转整数:")
print(f"原列表: {string_numbers}")
print(f"结果: {result}")
print()

# ===== reduce 函数 =====
# reduce 将列表中的元素逐个合并，最终返回一个值
from functools import reduce

# 例子 1: 计算列表中所有数字的和
numbers = [1, 2, 3, 4, 5]

def add(x, y):
    return x + y

result = reduce(add, numbers)
print("reduce 例子 1 - 求和:")
print(f"列表: {numbers}")
print(f"结果: {result}")
print()

# 例子 2: 计算列表中所有数字的乘积
def multiply(x, y):
    return x * y

result = reduce(multiply, numbers)
print("reduce 例子 2 - 求乘积:")
print(f"列表: {numbers}")
print(f"结果: {result}")
print()

# 例子 3: 找到列表中的最大值
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

def find_max(x, y):
    if x > y:
        return x
    else:
        return y

result = reduce(find_max, numbers)
print("reduce 例子 3 - 找最大值:")
print(f"列表: {numbers}")
print(f"结果: {result}")
print()

# ===== map 和 reduce 配合使用 =====
# 先用 map 转换数据，再用 reduce 汇总

print("map 和 reduce 配合使用:")
numbers = [1, 2, 3, 4, 5]
print(f"原列表: {numbers}")

# 第一步: 用 map 将每个数字乘以 2
doubled = list(map(lambda x: x * 2, numbers))
print(f"乘以 2 后: {doubled}")

# 第二步: 用 reduce 求和
total = reduce(lambda x, y: x + y, doubled)
print(f"求和结果: {total}")
