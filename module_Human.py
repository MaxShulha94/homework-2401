class Human:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def info(self):
        return 'Human'

    def __str__(self):
        return f'{self.surname}, {self.name}, {self.age}'
