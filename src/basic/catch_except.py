# Python 异常捕获基础教学

# 1. 基本的 try-except 结构
print("=== 1. 基本异常捕获 ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("错误：不能除以零")

# 2. 捕获多种异常
print("\n=== 2. 捕获多种异常 ===")
try:
    num = int("abc")
except (ValueError, TypeError):
    print("错误：无法转换为整数")

# 3. 使用 else 语句
print("\n=== 3. try-except-else ===")
try:
    num = int("123")
except ValueError:
    print("转换失败")
else:
    print(f"转换成功：{num}")

# 4. 使用 finally 语句
print("\n=== 4. try-except-finally ===")
try:
    f = open("test.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("文件不存在")
finally:
    print("清理资源")

# 5. 获取异常信息
print("\n=== 5. 获取异常详细信息 ===")
try:
    x = [1, 2, 3]
    print(x[10])
except IndexError as e:
    print(f"异常类型：{type(e).__name__}")
    print(f"异常信息：{e}")

# 6. 自定义异常
print("\n=== 6. 自定义异常 ===")
class AgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise AgeError("年龄不能为负数")
    return age

try:
    check_age(-5)
except AgeError as e:
    print(f"自定义异常：{e}")

# 7. 捕获所有异常（不推荐）
print("\n=== 7. 捕获所有异常 ===")
try:
    result = 10 / 0
except Exception as e:
    print(f"捕获到异常：{e}")