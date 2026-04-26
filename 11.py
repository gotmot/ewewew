class Student:
    def __init__(self, student_id, name, grade):
        self._id = student_id
        self.name = name
        self.grade = grade

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Ошибка: Имя не может быть пустым")
        self._name = value

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self._grade = value
        else:
            raise ValueError("Ошибка: Оценка должна быть от 0 до 100")

    def save(self):
        print(f"Сохранение студента: ID={self._id}, Имя={self._name}, Оценка={self._grade}")
try:
    student = Student(1, "Иван Иванов", 85)

    student.name = "Петр Петров"
    student.grade = 90

    student.save()

except ValueError as e:
    print(e)
