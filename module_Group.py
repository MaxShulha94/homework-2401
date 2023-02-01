import module_Student, module_logging

class GroupIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __next__(self):
        if self.index < len(self.students):
            self.index += 1
            return self.students[self.index - 1]
        raise StopIteration

class Group:
    def __init__(self, specialize, limit_st=10):
        self.specialize = specialize
        self.limit_st = limit_st
        self.students = []

    def __iter__(self):
        return GroupIterator(self.students)

    def __getitem__(self, item):
        return self.students[item]

    def __len__(self):
        return len(self.students)

    def add_st(self, student: module_Student.Student):
        if len(self.students) > self.limit_st:
            raise module_logging.LimitError('You can not add more than 10 students!')
        if student not in self.students:
            module_logging.logger.debug(f'Student {student} was added')
            self.students.append(student)

    def del_st(self, student: module_Student.Student):
        if student in self.students:
            self.students.remove(student)

    def search_st(self, surname: str):
        res = []
        for i in self.students:
            if i.surname == surname:
                res.append(i)
        return res

    def __str__(self):
        return f'{self.specialize}:\n' + '\n'.join(map(str, self.students))

