from student import Student
from university import University
from event import ApplicationSentEvent, ApplicationAcceptedEvent, ApplicationRejectedEvent

def main():
    # Create a student and university
    student1 = Student(name="Alice", age=20, student_id="S123")
    university = University(name="Tech University")

    # Student applies to the university
    student1.apply_to_university(university)

    # Process all communication events
    university.process_communications()

if __name__ == "__main__":
    main()