
"""
匿名函数 (lambda) 教学示例

覆盖内容：
- 基本语法
- 作为函数参数（map, filter, sorted, reduce）
- 闭包与返回 lambda
- 注意事项：不能包含语句，仅限表达式
"""

from functools import reduce


def basic_examples():
	# 基本用法：简单表达式
	add = lambda x, y: x + y
	print('add(2,3)=', add(2, 3))

	# 用于短小的即时函数
	print('square of 5 =', (lambda x: x * x)(5))


def as_parameters():
	nums = [1, 2, 3, 4, 5, 6]

	# map: 对每个元素应用函数
	squares = list(map(lambda x: x * x, nums))
	print('squares =', squares)

	# filter: 过滤符合条件的元素
	evens = list(filter(lambda x: x % 2 == 0, nums))
	print('evens =', evens)

	# reduce: 把序列归约为单个值
	sum_all = reduce(lambda a, b: a + b, nums)
	print('sum_all =', sum_all)

	# sorted: 按自定义 key 排序
	points = [(1, 2), (3, 1), (0, 0)]
	by_y = sorted(points, key=lambda p: p[1])
	print('sorted by y =', by_y)


def closures_and_returning_lambda():
	# 返回 lambda，形成闭包
	def make_multiplier(n):
		return lambda x: x * n

	doubler = make_multiplier(2)
	tripler = make_multiplier(3)
	print('doubler(5)=', doubler(5))
	print('tripler(5)=', tripler(5))


def common_patterns():
	# 在列表推导/匿名函数中结合条件表达式
	nums = range(-3, 4)
	abs_vals = list(map(lambda x: x if x >= 0 else -x, nums))
	print('abs_vals =', abs_vals)

	# 组合 lambda（函数式风格）
	inc = lambda x: x + 1
	square = lambda x: x * x
	compose = lambda f, g: lambda x: f(g(x))
	inc_then_square = compose(square, inc)
	print('inc_then_square(3)=', inc_then_square(3))


def pitfalls():
	# lambda 不能包含语句（如赋值、for、if 语句块等）
	# 如果逻辑复杂，优先使用 def 定义命名函数
	long_logic = lambda x: x * 2  # 简短示例
	print('long_logic(4)=', long_logic(4))


if __name__ == '__main__':
	basic_examples()
	as_parameters()
	closures_and_returning_lambda()
	common_patterns()
	pitfalls()
