"""
__getattr__ 教学代码
当访问对象不存在的属性时，会调用 __getattr__ 方法
"""


# 例子1：基础用法
class Student:
    def __init__(self,name):
        self.name = name

    def __getattr__(self, item):
        """当属性不存在时调用"""
        return f"属性 '{item}' 不存在"
    
def func_demo1():
    print("--- 例子1: 基础用法 ---")
    student = Student('张三')
    print(student.name)
    print(student.age)


# 例子2: 动态属性访问
class DynamicUser:
    def __init__(self, **kwargs):
        self._data = kwargs

    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"'{type(self).__name__}' 对象没有属性 '{name}'")

def func_demo2():
    print("\n--- 例子2: 动态属性访问 ---")
    user = DynamicUser(username='John', email='john@example.com')
    print(user.username)
    print(user.email)


# 例子3：链式调用
class ChainCall:
    def __getattr__(self, name):
        """支持链式调用"""
        def method(*args, **kwargs):
            print(f'调用了方法：{name}')
            return self
        return method
    
def func_demo3():
    print("\n--- 例子3: 链式调用 ---")
    chain = ChainCall()
    chain.method1().method2().method3()


# 例子4：代理对象
class Proxy:
    def __init__(self,obj):
        self._obj = obj

    def __getattr__(self, name):
        """代理对象的属性访问"""
        print(f"访问代理对象的属性:{name}")
        return getattr(self._obj, name)
    
def func_demo4():
    class original:
        def __init__(self):
            self.value = "原始对象"

    proxy = Proxy(original())
    print(proxy.value)


# execute
if __name__ == '__main__':
    func_demo1()
    func_demo2()
    func_demo3()
    func_demo4()