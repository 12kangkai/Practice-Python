
"""Python 返回函数 教学代码

示例包括：
- 返回一个简单的闭包
- 根据参数返回不同的函数
- 返回带状态的函数（使用非局部变量）
- 使用返回函数的装饰器示例
"""

from typing import Callable


def make_multiplier(n: int) -> Callable[[int], int]:
	"""返回一个将输入乘以 n 的函数（闭包示例）。"""
	def multiplier(x: int) -> int:
		return x * n

	return multiplier


def choose_operation(op: str) -> Callable[[int, int], int]:
	"""根据 op 返回不同的二元运算函数。"""
	if op == 'add':
		def add(a, b):
			return a + b

		return add
	elif op == 'mul':
		def mul(a, b):
			return a * b

		return mul
	else:
		def sub(a, b):
			return a - b

		return sub


def counter(start: int = 0) -> Callable[[], int]:
	"""返回一个带状态的计数器函数，演示 nonlocal。"""
	count = start

	def inc() -> int:
		nonlocal count
		count += 1
		return count

	return inc


def logging_decorator(func: Callable) -> Callable:
	"""一个简单的装饰器，它返回一个包装函数。"""
	def wrapper(*args, **kwargs):
		print(f"Calling {func.__name__} with", args, kwargs)
		result = func(*args, **kwargs)
		print(f"{func.__name__} returned", result)
		return result

	return wrapper


@logging_decorator
def add(a: int, b: int) -> int:
	return a + b


if __name__ == '__main__':
	# 闭包示例
	doubler = make_multiplier(2)
	print('doubler(5) ->', doubler(5))  # 10

	# 根据条件返回不同函数
	op = choose_operation('mul')
	print('3 * 4 ->', op(3, 4))

	# 带状态的函数
	c = counter(10)
	print(c())  # 11
	print(c())  # 12

	# 装饰器示例（装饰器本质上也是返回函数）
	print('add(2,3) ->', add(2, 3))
