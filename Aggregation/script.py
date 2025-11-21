"""
OOP Concept: AGGREGATION
------------------------
Aggregation = HAS-A relationship (weak ownership)
Teacher HAS Students.

But Students can exist without Teacher.
"""

# -----------------------------
# Student Class (Independent)
# -----------------------------
class Student:
    def __init__(self, name):
        self.name = name

    def get_student(self):
        return self.name


# -----------------------------
# Teacher Class (Aggregates Students)
# -----------------------------
class Teacher:
    def __init__(self, teacher_name, students_list):
        self.teacher_name = teacher_name
        self.students = students_list   # Aggregation: Teacher uses Student objects

    def show_details(self):
        print(f"Teacher Name: {self.teacher_name}")
        print("Students Under Teacher:")

        for student in self.students:
            print(f"- {student.get_student()}")


# -----------------------------
# Testing Aggregation
# -----------------------------
if __name__ == "__main__":
    # Students exist independently
    s1 = Student("Abdullah")
    s2 = Student("Ali")
    s3 = Student("Hamza")

    # Teacher aggregates existing students
    t = Teacher("Sir Ahmed", [s1, s2, s3])

    t.show_details()
