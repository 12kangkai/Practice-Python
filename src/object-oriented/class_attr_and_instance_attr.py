# 例1
class Animal:
    # 类属性
    species = 'Unknown'

    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.species}."


# 访问类属性
print('Animal species:', Animal.species)

# 创建实例
cat = Animal('Mimi', 2)
dog = Animal('Buddy', 4)

# 访问实例属性
print(cat.describe())
print(dog.describe())

# 修改实例属性
cat.age = 3
print('After updating cat age:', cat.describe())

# 修改类属性
Animal.species = 'Mammal'
print('Animal species after change:', Animal.species)
print(cat.describe())
print(dog.describe())

# 为某个实例创建同名属性，覆盖类属性
dog.species = 'Dog'
print('Dog instance species:', dog.species)
print('Cat instance species still:', cat.species)
print('Class species remains:', Animal.species)
print()


# 例2
class Student:

    '''统计学生人数,可以给Student类增加一个类属性,每创建一个实例,该属性自动增加'''
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')