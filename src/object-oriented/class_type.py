class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name}, {self.age} years old."


def print_object_info(obj):
    print(f"对象: {obj}")
    print("类型(type):", type(obj))
    print("类名(__class__.__name__):", obj.__class__.__name__)
    print("ID(id):", id(obj))
    print("是否为 Person:", isinstance(obj, Person))
    print("属性列表(dir):", [name for name in dir(obj) if not name.startswith("__")])
    print("数据属性(__dict__):", getattr(obj, "__dict__", {}))
    print()


if __name__ == "__main__":
    alice = Person("Alice", 28)
    print_object_info(alice)

    # 访问属性
    print("name:", getattr(alice, "name"))
    print("age:", getattr(alice, "age"))

    # 修改属性
    if hasattr(alice, "age"):
        setattr(alice, "age", 29)
    print("修改后的 age:", alice.age)

    # 判断方法
    print("是否具有 greet 方法:", hasattr(alice, "greet"))
    print("调用 greet():", alice.greet())
