import datetime

# Describe a class USER
class User:
    def __init__(self, last_name, first_name, middle_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.phone_number = phone_number

    def show_fullname(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


class Teacher(User):

    def __init__(self, last_name, first_name, middle_name, phone_number, school_address):
        super().__init__(last_name, first_name, middle_name, phone_number)
        self.school_address = school_address
        self.__created_tests__ = []
        self.given_score = {}

    def show_respectful_name(self):
        return f'{self.first_name} {self.middle_name}'

    def create_test(self, title, description):
        new_test = Test(title, description)
        new_test.creator = self.show_fullname()
        self.__created_tests__.append(new_test)
        return new_test

    def give_score(self, student, test, score, description):
        test_score = Score(student, self, test, score, description)
        self.given_score[(test_score.score_dt, student)] = [test.title, test_score.score]
        # student.taken_tests[(test, test_score.score_dt)] = score
        print('Оценка успешно выставлена.')


class Student(User):
    def __init__(self, last_name, first_name, middle_name, phone_number, birthday):
        super().__init__(last_name, first_name, middle_name, phone_number)
        self.birthday = birthday
        self.taken_tests = {}

    def take_test(self, test):
        test.participator.append(self)
        test_dt = datetime.datetime.now()
        # self.taken_tests[(test_dt, test)] = {'score': 99, 'score_dt': None, 'description': 'in_progress'}

    def __str__(self):
        return f'{self.show_fullname()} {self.birthday}'


class Test:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.create_time = datetime.datetime.now()
        self.creator = ''
        self.participator = []

    def __str__(self):
        return f'{self.title}, {self.create_time}'


class Score:
    def __init__(self, student, teacher, test, score, description):
        self.student = student
        self.teacher = teacher
        self.test = test
        self.score = score
        self.description = description
        self.score_dt = datetime.datetime.now()


teacher1 = Teacher('Лопаткин', 'Никита', 'Евгеньевич', '79154732330', 'Долгопрудный, Молодёжная улица, 10А')

test1 = teacher1.create_test('Математика', 'Таблица умножения')
test2 = teacher1.create_test('Русский язык', 'ЖИ-ШИ пиши с буквой И')

student1 = Student('Мирошниченко', 'Валерия', 'Алексеевна', '79264749971', '1992-06-02')
student2 = Student('Висич', 'Олеся', 'Игоревн', '79991112233', '2003-06-17')

student1.take_test(test1)
student2.take_test(test1)
student1.take_test(test2)

print(test1.participator)
print(test2.participator)

print(student1.taken_tests)
# print(teacher1.given_score)

teacher1.give_score(student2, test2, 3, 'Нужно стараться лучше!')
print(teacher1.given_score)
print(student1.taken_tests)
# test_score = Score(student1, teacher1, test1, 3, 'Нужно стараться лучше!')
# print(test_score.score_dt)

# dict1 = {}
# dict1[(datetime.datetime.now(), student1)] = ['Нужно стараться лучше!', 3]
# print(dict1)
