"""
杨辉三角(帕斯卡三角) - Yang Hui's Triangle (Pascal's Triangle)
"""


def yang_hui_triangle(n):
    """
    生成杨辉三角的前n行
    
    Args:
        n: 三角形的行数
    
    Returns:
        返回包含杨辉三角的二维列表
    """
    if n <= 0:
        return []
    
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)
    
    return triangle


def yang_hui_triangle_gen(n):
    """
    生成器方式生成杨辉三角的前n行，每次yield一行
    """
    if n <= 0:
        return

    row = [1]
    yield row
    for i in range(1, n):
        # 通过在两侧补0然后相邻元素相加生成下一行
        row = [x + y for x, y in zip([0] + row, row + [0])]
        yield row


def print_yang_hui_triangle(n):
    """
    打印杨辉三角
    
    Args:
        n: 三角形的行数
    """
    # 使用生成器逐行生成以降低内存占用
    for i, row in enumerate(yang_hui_triangle_gen(n)):
        # 计算空格用于居中显示
        spaces = ' ' * (n - i - 1)
        print(spaces + ' '.join(map(str, row)))


# 测试
if __name__ == '__main__':
    print("杨辉三角 (前10行):")
    print_yang_hui_triangle(10)
    print("\n")
    
    print("杨辉三角数据结构:")
    triangle = yang_hui_triangle(5)
    for row in triangle:
        print(row)
