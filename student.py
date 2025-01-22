# student.py

import uuid
from event import ApplicationSentEvent

class Student:
    def __init__(self, name, age, student_id=None):
        self.name = name
        self.age = age
        self.student_id = student_id if student_id else str(uuid.uuid4())
        self.application_status = None

    def apply_to_university(self, university):
        print(f"{self.name} is applying to {university.name}.")
        event = ApplicationSentEvent(self, university)
        university.communication_queue.put(event)
