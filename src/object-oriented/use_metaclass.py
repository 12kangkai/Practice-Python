"""
Python 元类（Metaclass）教学
元类是"类的类"，用于控制类的创建过程
"""

# ============ 1. 基础元类概念 ============

# 普通类是对象的蓝图，元类是类的蓝图
class SimpleMeta(type):
    """最简单的元类，展示元类如何拦截类的创建"""
    
    def __new__(mcs, name, bases, namespace):
        print(f"创建类: {name}")
        return super().__new__(mcs, name, bases, namespace)


# 使用元类创建类
class MyClass(metaclass=SimpleMeta):
    """使用SimpleMeta元类创建的类"""
    pass


# ============ 2. 元类中的三个关键方法 ============

class DetailedMeta(type):
    """展示元类的三个关键方法"""
    
    def __new__(mcs, name, bases, namespace):
        """创建类对象"""
        print(f"__new__ 被调用: 创建类 '{name}'")
        print(f"  基类: {bases}")
        print(f"  成员: {list(namespace.keys())}")
        
        # 可以修改namespace中的内容
        namespace['created_by_meta'] = True
        
        return super().__new__(mcs, name, bases, namespace)
    
    def __init__(cls, name, bases, namespace):
        """初始化类对象"""
        print(f"__init__ 被调用: 初始化类 '{name}'")
        super().__init__(name, bases, namespace)
    
    def __call__(cls, *args, **kwargs):
        """创建类的实例"""
        print(f"__call__ 被调用: 创建 {cls.__name__} 的实例")
        instance = super().__call__(*args, **kwargs)
        return instance


class DetailedClass(metaclass=DetailedMeta):
    """使用DetailedMeta元类的类"""
    
    def __init__(self, value):
        self.value = value


# ============ 3. 实用案例：单例模式（Singleton） ============

class SingletonMeta(type):
    """实现单例模式的元类"""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """单例数据库连接"""
    
    def __init__(self):
        self.connection = None
        print("Database 已初始化")
    
    def connect(self):
        self.connection = "Connected to DB"
        return self.connection


# ============ 4. 实用案例：自动注册（Auto Registration） ============

class RegistryMeta(type):
    """自动注册类到注册表"""
    
    registry = {}
    
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        
        # 除了RegistryMeta本身，将所有类都注册
        if name != 'RegisteredBase':
            mcs.registry[name] = cls
            print(f"类 '{name}' 已自动注册")
        
        return cls
    
    @classmethod
    def get_registry(mcs):
        """获取所有已注册的类"""
        return mcs.registry


class RegisteredBase(metaclass=RegistryMeta):
    """所有使用此元类的类都会自动注册"""
    pass


class UserService(RegisteredBase):
    pass


class OrderService(RegisteredBase):
    pass


class PaymentService(RegisteredBase):
    pass


# ============ 5. 实用案例：ORM 风格的属性验证 ============

class Field:
    """字段描述符"""
    
    def __init__(self, field_type, **kwargs):
        self.field_type = field_type
        self.required = kwargs.get('required', False)
        self.default = kwargs.get('default', None)


class ORMMeta(type):
    """ORM 元类，用于验证和处理字段"""
    
    def __new__(mcs, name, bases, namespace):
        fields = {}
        
        # 提取所有Field类型的属性
        for key, value in list(namespace.items()):
            if isinstance(value, Field):
                fields[key] = value
                # 移除Field定义，不在类中存储
                del namespace[key]
        
        namespace['_fields'] = fields
        
        cls = super().__new__(mcs, name, bases, namespace)
        return cls


class Model(metaclass=ORMMeta):
    """ORM 模型基类"""
    
    def __init__(self, **kwargs):
        for field_name, field in self._fields.items():
            value = kwargs.get(field_name, field.default)
            
            if field.required and value is None:
                raise ValueError(f"字段 '{field_name}' 是必需的")
            
            if value is not None and not isinstance(value, field.field_type):
                raise TypeError(f"字段 '{field_name}' 必须是 {field.field_type.__name__} 类型")
            
            setattr(self, field_name, value)


class User(Model):
    """用户模型"""
    name = Field(str, required=True)
    age = Field(int, default=18)
    email = Field(str, required=False)


# ============ 演示和测试 ============

if __name__ == "__main__":
    print("=" * 50)
    print("1. 基础元类演示")
    print("=" * 50)
    obj1 = MyClass()
    
    print("\n" + "=" * 50)
    print("2. 详细的元类方法演示")
    print("=" * 50)
    obj2 = DetailedClass(42)
    print(f"DetailedClass.created_by_meta: {DetailedClass.created_by_meta}")
    
    print("\n" + "=" * 50)
    print("3. 单例模式演示")
    print("=" * 50)
    db1 = Database()
    db2 = Database()
    print(f"db1 是 db2: {db1 is db2}")  # True
    print(f"db1.connect(): {db1.connect()}")
    
    print("\n" + "=" * 50)
    print("4. 自动注册演示")
    print("=" * 50)
    print(f"注册表: {RegistryMeta.get_registry()}")
    
    print("\n" + "=" * 50)
    print("5. ORM 风格验证演示")
    print("=" * 50)
    try:
        user = User(name="张三", age=25, email="zhangsan@example.com")
        print(f"创建用户成功: {user.name}, {user.age} 岁")
    except Exception as e:
        print(f"错误: {e}")
    
    try:
        user2 = User(age=30)  # 缺少必需的 name 字段
    except ValueError as e:
        print(f"验证错误: {e}")
