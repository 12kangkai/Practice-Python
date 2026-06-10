class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        ''' override tostring '''
        return 'Student object (name: %s)' % self.name

if __name__ == '__main__':

    print(Student('Kai'))

    s = Student('Kai')
    print(s.__repr__())

    # __str__ vs __repr__ teaching example
    print('\n--- __str__ vs __repr__ ---')
    
    # __str__: called by print() and str(), returns user-friendly string
    print('Using print():', s)  # calls __str__
    print('Using str():', str(s))  # calls __str__
    
    # __repr__: called by repr() and in interactive mode, returns developer-friendly string
    print('Using repr():', repr(s))  # calls __repr__
    
    # If __repr__ is not defined, it falls back to default object representation
    print('\n--- Key differences ---')
    print('str() is meant for end users: readable format')
    print('repr() is meant for developers: unambiguous representation')
    print('If __str__ is not defined, Python uses __repr__ as fallback')




    