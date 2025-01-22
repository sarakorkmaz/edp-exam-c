# main.py

from typing import List
from queue import Queue


# Event Class (Parent)
class Event:
    def __init__(self, payload):
        self.payload = payload


# Child Event Classes
class ApplicationSentEvent(Event):
    def __init__(self, student, university):
        super().__init__(payload={"student": student, "university": university})


class ApplicationAcceptedEvent(Event):
    def __init__(self, student, university):
        super().__init__(payload={"student": student, "university": university})


class ApplicationRejectedEvent(Event):
    def __init__(self, student, university):
        super().__init__(payload={"student": student, "university": university})


# Student Class
class Student:
    def __init__(self, name: str, age: int, student_id: str):
        self.name = name
        self.age = age
        self.student_id = student_id

    def apply_to_university(self, university):
        event = ApplicationSentEvent(self, university)
        university.handle_event(event)


# University Class
class University:
    def __init__(self, name: str):
        self.name = name
        self.communication_queue = Queue()

    def handle_event(self, event: Event):
        # Simulate acceptance or rejection
        if isinstance(event, ApplicationSentEvent):
            if event.payload["student"].age > 18:
                self.accept_student(event.payload["student"])
            else:
                self.reject_student(event.payload["student"])

    def accept_student(self, student):
        print(f"University {self.name}: Application from {student.name} accepted!")
        event = ApplicationAcceptedEvent(student, self)
        self.communication_queue.put(event)

    def reject_student(self, student):
        print(f"University {self.name}: Application from {student.name} rejected!")
        event = ApplicationRejectedEvent(student, self)
        self.communication_queue.put(event)

    def process_communications(self):
        while not self.communication_queue.empty():
            event = self.communication_queue.get()
            if isinstance(event, ApplicationAcceptedEvent):
                print(f"Processing accepted event for {event.payload['student'].name}")
            elif isinstance(event, ApplicationRejectedEvent):
                print(f"Processing rejected event for {event.payload['student'].name}")


# Demonstration in main.py

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
