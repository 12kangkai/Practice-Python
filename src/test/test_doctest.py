import doctest

"""
Python doctest 教学示例
doctest 是 Python 的一个测试框架,可以直接在文档字符串中编写测试用例
"""


def add(a, b):
    """
    计算两个数的和
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(0, 0)
        0
    """
    return a + b


def greet(name):
    """
    返回一个问候消息
    
    Examples:
        >>> greet('Alice')
        'Hello, Alice!'
        >>> greet('Bob')
        'Hello, Bob!'
    """
    return f"Hello, {name}!"


def divide(a, b):
    """
    计算两个数的商
    
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
        >>> divide(5, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero
    """
    return a / b


if __name__ == "__main__":
    # 运行所有 doctest 用例
    doctest.testmod(verbose=True)