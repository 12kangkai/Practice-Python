
"""__call__ 教学示例

演示如何为类实现 __call__, 使其实例像函数一样被调用。
"""

from typing import Any


class Multiplier:
	"""一个简单的可调用类，初始化时指定乘数，调用时对输入值相乘。"""

	def __init__(self, factor: float) -> None:
		self.factor = factor

	def __call__(self, value: float) -> float:
		"""将 value 与初始化时的 factor 相乘并返回结果。"""
		return value * self.factor


def demo() -> None:
	m2 = Multiplier(2)
	m3 = Multiplier(3)

	# 实例像函数一样被调用
	print('2 * 5 =', m2(5))   # 输出 10
	print('3 * 5 =', m3(5))   # 输出 15

	# 可以将可调用实例传递给期望可调用对象的地方
	funcs = [m2, m3, lambda x: x + 1]
	values = [1, 2, 3]
	results = [[f(v) for v in values] for f in funcs]
	print('results:', results)


if __name__ == '__main__':
	demo()
