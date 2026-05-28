
"""
Python 3.10+ 的 match / case (结构化模式匹配) 教学示例。

运行示例: python match_test.py
"""

def match_literal(value):
	match value:
		case 0:
			return "zero"
		case 1 | 2:
			return "one or two"
		case _:
			return "something else"


def match_sequence(seq):
	match seq:
		case [x, y]:
			return f"two-item list: {x}, {y}"
		case [x, *rest]:
			return f"first: {x}, rest: {rest}"
		case []:
			return "empty list"
		case _:
			return "not a list pattern"


def match_mapping(obj):
	match obj:
		case {"type": "point", "x": x, "y": y}:
			return f"Point at ({x}, {y})"
		case {"type": "circle", "r": r}:
			return f"Circle radius {r}"
		case _:
			return "unknown shape"


def match_class(obj):
	# 对象模式示例，使用属性名（需要类有相应的属性）
	match obj:
		case Point(x, y):
			return f"Point class: ({x}, {y})"
		case _:
			return "not a Point instance"


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# 为类启用属性模式，需要定义 __match_args__
	__match_args__ = ("x", "y")


def guard_examples(value):
	match value:
		case int(x) if x > 0:
			return "positive int"
		case int(x) if x < 0:
			return "negative int"
		case _:
			return "other"


def main():
	print("literal:", match_literal(2))
	print("sequence:", match_sequence([1, 2, 3]))
	print("mapping:", match_mapping({"type": "point", "x": 10, "y": 20}))
	p = Point(4, 5)
	print("class:", match_class(p))
	print("guard:", guard_examples(-3))


if __name__ == "__main__":
	main()
