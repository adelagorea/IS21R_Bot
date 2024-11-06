class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def student_details(self):
        return f"Student {self.name}, Age: {self.age}, ID: {self.student_id}"

# Testează clasele
student = Student("Alice", 20, "S12345")
print(student.student_details())  # Output: Student Alice, Age: 20, ID: S12345
