# Python dict and set 教学代码

# 字典 dict 示例
person = {
    "name": "Alice",
    "age": 30,
    "city": "Beijing"
}

print("字典内容:", person)
print("name:", person["name"])
print("age:", person.get("age"))

# 更新字段
person["age"] = 31
person["email"] = "alice@example.com"
print("更新后:", person)

# 删除字段
age = person.pop("age")
print("删除 age 后的字典:", person)
print("被删除的 age:", age)

# 遍历字典
for key, value in person.items():
    print(f"{key} -> {value}")

print("-----")

# 集合 set 示例
fruits = {"apple", "banana", "orange"}
print("集合内容:", fruits)

# 添加和删除元素
fruits.add("pear")
fruits.discard("banana")
print("修改后集合:", fruits)

# 集合操作
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("交集:", a & b)
print("并集:", a | b)
print("差集:", a - b)
print("对称差集:", a ^ b)

# 使用集合去重
numbers = [1, 2, 2, 3, 3, 3]
unique = set(numbers)
print("原始列表:", numbers)
print("去重后集合:", unique)
