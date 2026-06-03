# 装饰器示例

def debug(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result
    return wrapper

def debug_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{prefix} Calling {func.__name__} with args={args}, kwargs={kwargs}')
            result = func(*args, **kwargs)
            print(f'{prefix} {func.__name__} returned {result}')
            return result
        return wrapper
    return decorator

@debug
def add(a, b):
    return a + b


@debug
def greet(name='world'):
    return f'Hello, {name}!'

@debug_prefix('[DEBUG]')
def add_with_prefix(a, b):
    return a + b

if __name__ == '__main__':
    print('add(3, 5):', add(3, 5))
    print(greet())
    print(greet(name='Python'))

    print('-' * 20)
    add_with_prefix(10, 20)