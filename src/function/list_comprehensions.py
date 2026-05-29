# list_comprehensions.py
# Python 列表生成式（List Comprehension）语法教学示例

# 1. 最简单的列表生成式：生成 0 到 9 的平方数
squares = [x * x for x in range(10)]

# 2. 带条件筛选：只保留偶数的平方
even_squares = [x * x for x in range(10) if x % 2 == 0]

# 3. 条件表达式：偶数保留原值，奇数取相反数
conditional_values = [x if x % 2 == 0 else -x for x in range(1, 11)]

# 4. 嵌套循环生成式：生成坐标对
pairs = [(x, y) for x in range(3) for y in range(3)]

# 5. 对已有列表做变换：将水果名称转换为大写
fruits = ['apple', 'banana', 'cherry']
upper_fruits = [fruit.upper() for fruit in fruits]

# 6. 结合字典使用生成式：只保留值大于 1 的条目
items = {'a': 1, 'b': 2, 'c': 3}
pairs_from_dict = [f"{k}:{v}" for k, v in items.items() if v > 1]

# 7. 列表生成式也可以嵌入函数调用
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes_under_20 = [x for x in range(20) if is_prime(x)]

if __name__ == '__main__':
    print('squares:', squares)
    print('even_squares:', even_squares)
    print('conditional_values:', conditional_values)
    print('pairs:', pairs)
    print('upper_fruits:', upper_fruits)
    print('pairs_from_dict:', pairs_from_dict)
    print('primes_under_20:', primes_under_20)

