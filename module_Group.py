import module_Student, module_logging

class GroupIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __next__(self):
        if self.index < self.students:
            self.index += 1
            return self.students[self.index - 1]
        raise StopIteration

class Group:
    def __init__(self, specialize, limit_st=10):
        self.specialize = specialize
        self.limit_st = limit_st
        self.list_group = []

    def __iter__(self):
        return GroupIterator(self.list_group)

    def __getitem__(self, item):
        return self.list_group[item]

    def __len__(self):
        return len(self.list_group)

    def add_st(self, student: module_Student.Student):
        if len(self.list_group) > self.limit_st:
            raise module_logging.LimitError('You can not add more than 10 students!')
        if student not in self.list_group:
            module_logging.logger.debug(f'Student {student} was added')
            self.list_group.append(student)

    def del_st(self, student: module_Student.Student):
        if student in self.list_group:
            self.list_group.remove(student)

    def search_st(self, surname: str):
        res = []
        for i in self.list_group:
            if i.surname == surname:
                res.append(i)
        return res

    def __str__(self):
        return f'{self.specialize}:\n' + '\n'.join(map(str, self.list_group))