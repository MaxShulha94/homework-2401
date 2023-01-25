import module_Human
class Student(module_Human.Human):
    def __int__(self, surname, name, age):
        super().__init__(surname, name, age)

    def info(self):
        return 'Student'