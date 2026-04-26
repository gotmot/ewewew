class Employee:
    _database = {}

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Имя не может быть пустым")
        self._name = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self._salary = value

    def save(self):
        Employee._database[self.emp_id] = self.to_dict()
        print(f"Объект {self.name} сохранен.")

    def to_dict(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "salary": self.salary,
            "type": self.__class__.__name__
        }

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def assign_task(self, task_description):
        print(f"{self.name} (менеджер отдела {self.department}) назначена задача: {task_description}")

    def to_dict(self):
        data = super().to_dict()
        data["department"] = self.department
        return data
employee = Employee(1, "Иван Иванов", 50000)
employee.save()
manager = Manager(2, "Анна Сидорова", 80000, "IT")
manager.save()
manager.assign_task("Разработать новую фичу")
