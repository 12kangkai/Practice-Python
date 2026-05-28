"""Python 循环教学示例"""

# for 循环遍历列表
fruits = ["apple", "banana", "cherry"]
print("for 循环遍历列表:")
for fruit in fruits:
    print(f"- {fruit}")

# for 循环遍历字典
person = {"name": "Alice", "age": 30, "city": "Beijing"}
print("\nfor 循环遍历字典:")
for key, value in person.items():
    print(f"{key}: {value}")

# for 循环遍历字符串
message = "hello"
print("\nfor 循环遍历字符串:")
for ch in message:
    print(ch, end=" ")
print()

# range() 生成数值序列
print("\nrange() 生成数值序列:")
for i in range(1, 6):
    print(i, end=" ")
print()

# while 循环示例
print("\nwhile 循环示例:")
count = 3
while count > 0:
    print(f"倒计时: {count}")
    count -= 1

# break 和 continue
print("\nbreak 和 continue 示例:")
for i in range(1, 10):
    if i == 5:
        print("遇到 5，退出循环")
        break
    if i % 2 == 0:
        print(f"跳过偶数: {i}")
        continue
    print(f"当前值: {i}")

# 嵌套循环
print("\n嵌套循环示例:")
for x in range(1, 4):
    for y in range(1, 4):
        print(f"({x}, {y})", end=" ")
    print()
