from abc import ABC, abstractmethod

class SchoolMember(ABC):
    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def show(self) -> str:
        pass

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self) -> str:
        return f"Name: {self.name}, Age: {self.age} years old, Salary: {self.salary:.2f} USD"

class Student(SchoolMember):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    def show(self) -> str:
        return f"Name: {self.name}, Age: {self.age} years old, Grades: {self.grades} points"
