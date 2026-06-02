
"""
filter.py

Python filter 教学代码 - 示例展示如何使用内置 filter() 函数。

主要示例：
- 使用命名函数
- 使用 lambda
- 过滤假值（None 作为函数）
- 与 map / list / generator 一起使用

运行示例：直接运行此文件会打印各例子的结果。
"""

from typing import Iterable, Callable, List


def keep_even(n: int) -> bool:
	"""返回 n 是否为偶数。用于演示命名函数与 filter 一起使用。"""
	return n % 2 == 0


def example_named_function():
	nums = list(range(10))
	evens = list(filter(keep_even, nums))
	print('named function -> evens:', evens)


def example_lambda():
	nums = list(range(10))
	# 使用 lambda 等价于 keep_even
	evens = list(filter(lambda x: x % 2 == 0, nums))
	print('lambda -> evens:', evens)


def example_filter_none():
	items = [0, 1, '', 'hello', None, [], [1, 2], False, True]
	# 当第一个参数为 None 时，filter 会移除所有假值（falsy values）
	truthy = list(filter(None, items))
	print('filter(None) -> truthy values:', truthy)


def example_with_map():
	names = ['alice', 'Bob', '', 'charlie', None]
	# 先用 filter 去除 None / 空字符串，再用 map 统一首字母大写
	cleaned = map(lambda s: s.capitalize(), filter(None, names))
	print('filter + map ->', list(cleaned))


def example_generator():
	# filter 返回一个迭代器（惰性求值），可以用于内存敏感场景
	def is_prime(n: int) -> bool:
		if n < 2:
			return False
		for i in range(2, int(n ** 0.5) + 1):
			if n % i == 0:
				return False
		return True

	nums = range(100)
	primes_iter = filter(is_prime, nums)
	# 取前 10 个素数
	primes_first_10 = [next(primes_iter) for _ in range(10)]
	print('first 10 primes:', primes_first_10)


def example_custom_predicate():
	# 更复杂的过滤条件：保留字符串且长度 >= 3
	data = ['a', 'ab', 'abc', 'abcd', 123, None]
	def predicate(x):
		return isinstance(x, str) and len(x) >= 3

	result = list(filter(predicate, data))
	print('custom predicate ->', result)


def demo_all():
	example_named_function()
	example_lambda()
	example_filter_none()
	example_with_map()
	example_generator()
	example_custom_predicate()


if __name__ == '__main__':
	demo_all()
