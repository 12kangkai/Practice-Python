class Student(object):
    
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get__name(self):
        return self.__name



if __name__ == '__main__':

    stu = Student('张三',60)
    '''私有变量直接调用会报错: AttributeError: 'Student' object has no attribute '__name' '''
    # stu.__name

    '''这里并不是给初始化的私有变量__name赋值, 而是创建了一个非私有变量, 并赋值为New_Name '''
    stu.__name = 'New_Name'
    print(stu.__name)

    '''私有变量间接调用, 实际开发中, 建议使用get and set 进行封装'''
    print(f'{stu._Student__name}')

    b = stu.__name == stu.get__name()
    print(b)


        
        