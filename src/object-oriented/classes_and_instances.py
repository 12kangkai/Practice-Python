class Student(object):

    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    # def print_self(self):
    #     print(f'{bart.name} - {bart.sex}')

    def print_self(*args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)
        print(f'{bart.name} - {bart.sex}')


if __name__ == '__main__':
    bart = Student('A','男')
    print(bart)
    print()

    print('-' * 20)

    bart.print_self()
    bart.name = '张三'
    bart.print_self()

    print('-' * 20)

    method = bart.print_self
    print(method)
    print(method.__func__)
    print(method.__self__)

    method()

    print('-' * 20)

    print(Student.__dict__)
    print(type(Student.print_self))
    print(type(bart.print_self))


    
    
