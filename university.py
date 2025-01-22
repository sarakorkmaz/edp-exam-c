# university.py

from event import ApplicationAcceptedEvent, ApplicationRejectedEvent
from communication_queue import CommunicationQueue

class University:
    def __init__(self, name):
        self.name = name
        self.communication_queue = CommunicationQueue()  # Use the CommunicationQueue class

    def process_applications(self):
        while not self.communication_queue.empty():
            event = self.communication_queue.get()
            student = event.payload['student']
            print(f"Processing application for {student.name} from {self.name}. Event timestamp: {event.timestamp}")
            if student.age >= 18:
                student.application_status = "Accepted"
                print(f"Application Accepted for {student.name}.")
                accepted_event = ApplicationAcceptedEvent(student, self)
                self.communication_queue.put(accepted_event)
            else:
                student.application_status = "Rejected"
                print(f"Application Rejected for {student.name}.")
                rejected_event = ApplicationRejectedEvent(student, self)
                self.communication_queue.put(rejected_event)

