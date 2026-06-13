'''限制类的属性'''

class Student:
    __slots__ = ('name', 'age')

    def print_info(self):
        print(f'{self.name} - {self.age}')

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.name = 'Kai'
g.age = 26
g.score = 100
g.print_info()

s = Student()
s.name = 'Kai'
s.age = 26
s.score = 100
s.print_info()



