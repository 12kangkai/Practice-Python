class Animal(object):

    def run(self):
        print('Animal is running...')


class Dog(Animal):
    
    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


def run_twice(animal):
    """示例多态：相同接口，不同对象实现不同行为。"""
    animal.run()
    animal.run()


if __name__ == '__main__':

    animal = Animal()
    dog = Dog()
    cat = Cat()

    for obj in (animal, dog, cat):
        run_twice(obj)
        print('-' * 20)

    print(f'{isinstance(animal, Animal)}')
    print(f'{isinstance(cat, Cat)}')
    print(f'{isinstance(cat, Animal)}')
    print(f'{isinstance(dog, Dog)}')
    print(f'{isinstance(dog, Animal)}')

