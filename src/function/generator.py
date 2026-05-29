"""
Python 生成器（generator）教学

本文件以简洁的示例说明 Python 生成器的常用用法：
- 基本生成器函数（yield）
- 生成器表达式
- send()、throw()、close() 的用法
- 常见应用场景（延迟计算、处理流数据）

示例可直接运行观察输出。
"""

def simple_generator(n):
	"""生成 0..n-1 的值，每次迭代通过 yield 产生一个值。"""
	i = 0
	while i < n:
		yield i
		i += 1


def generator_send_example():
	"""示例：使用 send 向生成器传入值并作为结果返回。
	初始调用 next(g) 或 g.send(None) 启动生成器，后续可用 send 传值。
	"""
	def counter():
		total = 0
		while True:
			increment = yield total
			if increment is None:
				break
			total += increment

	g = counter()
	next(g)               # 启动生成器，运行到第一个 yield，返回初始 total(0)
	print(g.send(5))      # 发送 5，yield 返回更新前的 total (0)，函数继续执行，total 变为 5
	print(g.send(3))      # 同理，返回 5，然后 total 变为 8
	g.send(None)          # 发送 None 用作结束信号，生成器退出


def generator_throw_close():
	"""示例：throw 抛入异常到生成器内部，close 关闭生成器。"""
	def gen():
		try:
			yield 'start'
		except ValueError:
			yield 'caught ValueError'
		finally:
			# 清理代码
			print('generator finally')

	g = gen()
	print(next(g))        # 'start'
	print(g.throw(ValueError))
	try:
		g.close()
	except RuntimeError:
		pass


def generator_expression_example():
	# 生成器表达式更轻量，记住它不会立刻计算值
	gen_exp = (x * x for x in range(5))
	for v in gen_exp:
		print(v)


if __name__ == '__main__':
	print('simple_generator:')
	for x in simple_generator(3):
		print(x)

	print('\ngenerator_send_example:')
	generator_send_example()

	print('\ngenerator_throw_close:')
	generator_throw_close()

	print('\ngenerator_expression_example:')
	generator_expression_example()

