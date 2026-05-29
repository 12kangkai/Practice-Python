"""
Python 可迭代对象和迭代器教学
Iterables and Iterators Tutorial

核心概念:
1. Iterable (可迭代对象): 实现 __iter__() 方法,返回迭代器
2. Iterator (迭代器): 实现 __iter__() 和 __next__() 方法
3. 区别: 可迭代对象 -> 迭代器 -> 具体的值
"""

# ============ 1. 基础概念 ============
print("=" * 60)
print("1. Iterable vs Iterator")
print("=" * 60)

# Iterable: 列表、元组、字符串等
my_list = [1, 2, 3]
print(f"列表是可迭代对象: {hasattr(my_list, '__iter__')}")
print(f"列表有__next__吗: {hasattr(my_list, '__next__')}")

# Iterator: 通过iter()获得
my_iterator = iter(my_list)
print(f"迭代器是可迭代对象: {hasattr(my_iterator, '__iter__')}")
print(f"迭代器有__next__: {hasattr(my_iterator, '__next__')}")

print(f"第一个值: {next(my_iterator)}")
print(f"第二个值: {next(my_iterator)}")
print(f"第三个值: {next(my_iterator)}")
try:
    print(f"第四个值: {next(my_iterator)}")
except StopIteration:
    print("迭代完成，抛出 StopIteration 异常")


# ============ 2. 自定义可迭代类 ============
print("\n" + "=" * 60)
print("2. 自定义可迭代类")
print("=" * 60)

class CountUp:
    """自定义可迭代对象"""
    def __init__(self, max_num):
        self.max_num = max_num
    
    def __iter__(self):
        """返回迭代器"""
        return CountUpIterator(self.max_num)


class CountUpIterator:
    """自定义迭代器"""
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0
    
    def __iter__(self):
        """迭代器本身是可迭代的"""
        return self
    
    def __next__(self):
        """获取下一个值"""
        if self.current < self.max_num:
            self.current += 1
            return self.current
        else:
            raise StopIteration


count_up = CountUp(3)
print("使用自定义迭代器:")
for num in count_up:
    print(f"  {num}")


# ============ 3. 生成器函数 ============
print("\n" + "=" * 60)
print("3. 生成器函数 (Generator)")
print("=" * 60)

def count_up_generator(max_num):
    """生成器函数 - 最简洁的方式"""
    current = 0
    while current < max_num:
        current += 1
        print(f"yield 前，继续执行...")
        yield current
        print(f"yield 后，继续执行...\n")

print("使用生成器: ")
for num in count_up_generator(5):
    print(f"current = {num}")

# 生成器是迭代器
gen = count_up_generator(3)
print(f"生成器有__iter__: {hasattr(gen, '__iter__')}")
print(f"生成器有__next__: {hasattr(gen, '__next__')}")


# ============ 4. 无限迭代器 ============
print("\n" + "=" * 60)
print("4. 无限迭代器")
print("=" * 60)

def infinite_count():
    """无限计数生成器"""
    n = 0
    while True:
        yield n
        n += 1


print("使用无限生成器 (前5个):")
counter = infinite_count()
for _ in range(5):
    print(f"  {next(counter)}")


# ============ 5. 内置迭代工具 ============
print("\n" + "=" * 60)
print("5. 内置迭代工具")
print("=" * 60)

# map
print("map() - 转换每个元素:")
numbers = [1, 2, 3]
squared = map(lambda x: x ** 2, numbers)
print(f"  {list(squared)}")

# filter
print("filter() - 过滤元素:")
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(f"  {list(evens)}")

# zip
print("zip() - 并行迭代:")
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"  {name}: {age}")

# enumerate
print("enumerate() - 获取索引和值:")
for idx, name in enumerate(names):
    print(f"  {idx}: {name}")


# ============ 6. 对比 C# 的相同特性 ============
print("\n" + "=" * 60)
print("6. Python vs C# 对比")
print("=" * 60)

comparison = """
┌─────────────────────────────────────────────────────────────┐
│            Python               │         C#                 │
├──────────────────────────────────┼──────────────────────────┤
│ Iterable (可迭代对象)            │ IEnumerable              │
│ - 实现 __iter__()                │ - 实现 GetEnumerator()    │
│                                  │                          │
│ Iterator (迭代器)                │ IEnumerator              │
│ - 实现 __iter__() 和 __next__()   │ - 实现 MoveNext()        │
│                                  │   和 Current 属性        │
│                                  │                          │
│ for item in iterable:            │ foreach(var item in      │
│     ...                          │         enumerable) {...} │
│                                  │                          │
│ yield 关键字 (生成器)             │ yield 关键字 (迭代器)     │
│ def func():                      │ public IEnumerator      │
│     yield value                  │     GetEnumerator()     │
│                                  │ {                       │
│                                  │     yield return value; │
│                                  │ }                       │
│                                  │                          │
│ map(), filter(), zip()           │ LINQ 查询                │
│ list comprehension               │ (Select, Where, Join)   │
│                                  │                          │
│ StopIteration 异常               │ MoveNext() 返回 false     │
│                                  │                          │
│ 惰性求值 (Lazy Evaluation)       │ 惰性求值 (Lazy Query)    │
│ 生成器按需生成值                  │ LINQ 延迟执行            │
└──────────────────────────────────┴──────────────────────────┘

关键差异:
1. Python: 协议式 (duck typing) vs C#: 接口式 (IEnumerable)
2. Python: StopIteration vs C#: false from MoveNext()
3. Python: 原生支持惰性求值 vs C#: LINQ 提供
4. Python: 简洁的 yield vs C#: 需要实现接口和 yield return
"""

print(comparison)


# ============ 7. 实战示例 ============
print("=" * 60)
print("7. 实战示例")
print("=" * 60)

# 生成斐波那契数列
def fibonacci(n):
    """生成前n个斐波那契数"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


print("斐波那契数列 (前8个):")
fib_list = list(fibonacci(8))
print(f"  {fib_list}")

# 从文件中逐行读取 (模拟)
def file_reader(file_path, chunk_size=10):
    """模拟从文件读取 - 使用生成器处理大文件"""
    # 实际使用中可以逐行读取文件而不加载到内存
    lines = [
        "line 1\n", "line 2\n", "line 3\n",
        "line 4\n", "line 5\n", "line 6\n",
    ]
    for line in lines:
        yield line.strip()


print("文件迭代 (模拟):")
for i, line in enumerate(file_reader('dummy.txt')):
    if i < 3:  # 只显示前3行
        print(f"  {line}")


# 链式处理
print("\n链式处理 (惰性求值):")
numbers = range(1, 11)
result = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
print(f"  偶数的平方: {list(result)}")

print("\n" + "=" * 60)
print("总结")
print("=" * 60)
print("""
Python 迭代器是一种强大的编程模式:
1. ✓ 节省内存: 惰性求值,按需生成
2. ✓ 简洁优雅: yield 关键字简化代码
3. ✓ 统一接口: for 循环统一处理所有可迭代对象
4. ✓ 灵活扩展: 自定义类实现迭代协议

与 C# 的 IEnumerable 本质相同,但实现方式更 Pythonic!
""")
