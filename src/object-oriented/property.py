'''
语法糖：

@property
def xxx(self): ...

@xxx.setter
def xxx(self, value): ...

@xxx.deleter
def xxx(self): ...

'''

# 例1 基本用法
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        """获取温度"""
        print("Getting value...")
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        """设置温度"""
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        print("Setting value...")
        self._temperature = value

    @temperature.deleter
    def temperature(self):
        """删除温度"""
        print("Deleting value...")
        del self._temperature

c = Celsius(25)
print(c.temperature) #触发getter
c.temperature = 30 #触发setter
del c.temperature #触发deleter

print('_' * 20)

# 例2 只读计算属性
class Rectangle:
    
    def __init__(self, width=0,height=0):
        self.width=width
        self.height=height

    @property
    def area(self):
        """如果只定义 getter,不定义 setter 和 deleter,则属性是 只读的"""
        return self.width * self.height
    

r = Rectangle(3,4)
print(r.area)
print('_' * 20)

# 例3 延迟计算 Circle radius
class Circle:

    def __init__(self, radius=0):
        self.radius = radius
        self._area = None

    @property
    def area(self):
        """如果命中缓存,则返回缓存,无需重复计算"""
        if self._area is None:
            self._area = 3.14 * self.radius**2
        return self._area

c = Circle(2)
print(c.area)
print(c.area)
print('_' * 20)

# 例4 综合类型检查/数据验证
class Person:

    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

p = Person('Kai')
print(p.name)
p.name="Jane"
print(p.name)
p.name=123






