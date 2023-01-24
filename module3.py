import module2
class Student(module2.Human):
    def __int__(self, surname, name, age):
        super().__init__(surname, name, age)

    def info(self):
        return 'Student'