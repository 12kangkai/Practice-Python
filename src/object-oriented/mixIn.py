# mixIn.py
# 多重继承教学代码：演示 Python 中 mixin 类和方法解析顺序（MRO）

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def move(self):
        print(f"{self.name} is moving on land.")


class FlyMixin:
    def fly(self):
        print(f"{self.name} is flying.")

    def move(self):
        print(f"{self.name} is flying through the sky.")


class SwimMixin:
    def swim(self):
        print(f"{self.name} is swimming.")

    def move(self):
        print(f"{self.name} is swimming in the water.")


class Duck(FlyMixin, SwimMixin, Animal):
    def quack(self):
        print(f"{self.name} says quack!")


if __name__ == '__main__':
    donald = Duck('Donald')
    donald.eat()
    donald.fly()
    donald.swim()
    donald.quack()

    print('\nDuck MRO:')
    for cls in Duck.mro():
        print(' -', cls.__name__)

    print('\n移动行为 (调用 move 方法)：')
    donald.move()
