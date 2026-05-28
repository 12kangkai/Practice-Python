"""Python 函数教学代码示例。"""

# 1. 基本函数定义

def greet(name):
    """向指定的人打招呼。"""
    return f"你好，{name}！"


# 2. 带默认参数的函数

def power(base, exponent=2):
    """计算 base 的 exponent 次方。"""
    return base ** exponent


# 3. 可变位置参数和关键字参数

def summarize(*numbers, prefix="总和"):
    """计算输入数字的和，并添加前缀。"""
    total = sum(numbers)
    return f"{prefix}: {total}"


def build_profile(first_name, last_name, **info):
    """构建一个包含用户信息的字典。"""
    profile = {
        "first_name": first_name,
        "last_name": last_name,
    }
    profile.update(info)
    return profile


# 4. 递归函数示例

def factorial(n):
    """递归计算 n 的阶乘。"""
    if n < 0:
        raise ValueError("n 必须是非负整数")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


# 5. 主要函数入口

def main():
    print(greet("世界"))
    print(power(3))
    print(power(2, 5))
    print(summarize(1, 2, 3, 4, prefix="结果"))

    user = build_profile("李", "华", age=28, city="北京")
    print(user)
    print(f"5 的阶乘是: {factorial(5)}")


if __name__ == "__main__":
    main()
