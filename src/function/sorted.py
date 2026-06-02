
"""sorted() 教学示例

示例包括：基本用法、逆序、key 函数、对字典和自定义对象排序、稳定性演示。
"""

from operator import attrgetter


def basic_examples():
	# 基本用法：返回新列表，原列表不变
	nums = [5, 2, 9, 1]
	print('original:', nums)
	print('sorted:', sorted(nums))

	# 逆序
	print('sorted reverse:', sorted(nums, reverse=True))

	# 对字符串按字母排序
	words = ['banana', 'apple', 'cherry']
	print('words sorted:', sorted(words))


def key_examples():
	words = ['banana', 'apple', 'Cherry', 'date']
	# 忽略大小写排序
	print('case-insensitive:', sorted(words, key=str.lower))

	# 按长度排序
	print('by length:', sorted(words, key=len))

	# 复杂 key：先按长度再按字母
	print('by length then lexicographic:', sorted(words, key=lambda w: (len(w), w.lower())))


def dict_examples():
	# 对字典排序：items 返回 (key, value) 元组
	d = {'a': 3, 'b': 1, 'c': 2}
	# 按键排序
	print('dict keys sorted:', sorted(d))
	# 按值排序，返回键列表
	print('dict keys by value:', sorted(d, key=d.get))
	# 返回按值排序的 (key, value) 列表
	print('items by value:', sorted(d.items(), key=lambda iv: iv[1]))


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f"Person(name={self.name!r}, age={self.age})"


def object_examples():
	people = [Person('Alice', 30), Person('bob', 25), Person('Charlie', 25)]
	# 按属性排序
	print('by age:', sorted(people, key=attrgetter('age')))
	# 如果希望二次排序（年龄相同时按名字）
	print('by age then name:', sorted(people, key=lambda p: (p.age, p.name.lower())))


def stability_demo():
	# Python 的排序是稳定的：相等 key 的元素保留原始相对顺序
	items = [('a', 2), ('b', 1), ('c', 2), ('d', 1)]
	# 按第二个元素排序，1 的相对顺序为 b then d（和原序一致）
	print('stable sort demo:', sorted(items, key=lambda x: x[1]))


if __name__ == '__main__':
	basic_examples()
	print()
	key_examples()
	print()
	dict_examples()
	print()
	object_examples()
	print()
	stability_demo()
