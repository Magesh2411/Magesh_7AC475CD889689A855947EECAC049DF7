class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"{self.name} (Roll: {self.roll_number}, CGPA: {self.cgpa})"


def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
students = [
    Student("Alice", "A123", 3.8),
    Student("Bob", "B456", 3.5),
    Student("Charlie", "C789", 3.9),
    Student("David", "D101", 3.6),
]

sorted_students = sort_students(students)

print("Sorted Students by CGPA (Descending Order):")
for student in sorted_students:
    print(student)
