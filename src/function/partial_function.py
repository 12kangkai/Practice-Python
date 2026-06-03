"""
Python 偏函数 (Partial Function) 教学代码

偏函数是通过 functools.partial() 创建的，它允许我们固定一个函数的某些参数，
返回一个新的函数，这个新函数只需要提供剩余的参数。
"""

from functools import partial


# 示例 1: 基础偏函数
def add(x, y, z):
    """三个数相加"""
    return x + y + z


# 创建偏函数：固定第一个参数为 10
add_10 = partial(add, 10)
print("示例 1: 基础偏函数")
print(f"add_10(5, 3) = {add_10(5, 3)}")  # 输出: 18
print()


# 示例 2: 固定多个参数
multiply = lambda x, y, z: x * y * z
multiply_by_2_3 = partial(multiply, 2, 3)
print("示例 2: 固定多个参数")
print(f"multiply_by_2_3(4) = {multiply_by_2_3(4)}")  # 输出: 24
print()


# 示例 3: 使用关键字参数固定
def power(base, exponent):
    """计算 base 的 exponent 次方"""
    return base ** exponent


# 固定指数为 2（平方）
square = partial(power, exponent=2)
print("示例 3: 使用关键字参数")
print(f"square(5) = {square(5)}")  # 输出: 25
print()


# 示例 4: 与内置函数一起使用
print("示例 4: 与内置函数一起使用")
# 创建一个偏函数来转换十六进制字符串
int_base_16 = partial(int, base=16)
print(f"int_base_16('FF') = {int_base_16('FF')}")  # 输出: 255
print(f"int_base_16('1A') = {int_base_16('1A')}")  # 输出: 26
print()


# 示例 5: 实际应用 - 日志记录
def log(level, message):
    """记录日志消息"""
    return f"[{level}] {message}"


# 创建特定级别的日志函数
log_error = partial(log, "ERROR")
log_info = partial(log, "INFO")
log_debug = partial(log, "DEBUG")

print("示例 5: 实际应用 - 日志记录")
print(log_error("系统出错"))  # [ERROR] 系统出错
print(log_info("程序正常运行"))  # [INFO] 程序正常运行
print(log_debug("调试信息"))  # [DEBUG] 调试信息
print()


# 示例 6: 偏函数的属性
print("示例 6: 偏函数的属性")
divide = lambda x, y: x / y
divide_by_10 = partial(divide, y=10)
print(f"func: {divide_by_10.func}")  # 原始函数
print(f"args: {divide_by_10.args}")  # 固定的位置参数
print(f"keywords: {divide_by_10.keywords}")  # 固定的关键字参数
print(f"divide_by_10(100) = {divide_by_10(100)}")  # 输出: 10.0
print()


# 示例 7: 比较偏函数与 lambda 表达式
print("示例 7: 偏函数 vs Lambda 表达式")

def greet(greeting, name):
    return f"{greeting}, {name}!"


# 使用偏函数
greet_hello = partial(greet, "Hello")

# 使用 lambda 表达式
greet_hello_lambda = lambda name: greet("Hello", name)

print(f"partial: {greet_hello('Alice')}")  # Hello, Alice!
print(f"lambda: {greet_hello_lambda('Alice')}")  # Hello, Alice!
print()


# 示例 8: 偏函数在 map、filter 中的应用
print("示例 8: 偏函数在高阶函数中的应用")

def multiply_by_n(n, x):
    return n * x


# 创建偏函数
multiply_by_3 = partial(multiply_by_n, 3)

# 使用 map 应用偏函数
numbers = [1, 2, 3, 4, 5]
result = list(map(multiply_by_3, numbers))
print(f"乘以 3: {result}")  # [3, 6, 9, 12, 15]
