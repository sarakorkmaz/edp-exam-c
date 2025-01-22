# main.py

from student import Student
from university import University

# Demonstration of the system
if __name__ == "__main__":
    # Create students and university
    student1 = Student(name="Alice", age=20)
    student2 = Student(name="Bob", age=17)

    university = University(name="Oxford University")

    # Students apply to the university
    student1.apply_to_university(university)
    student2.apply_to_university(university)

    # University processes applications
    university.process_applications()

    # Check final status of students
    print(f"Final status of {student1.name}: {student1.application_status}")
    print(f"Final status of {student2.name}: {student2.application_status}")
