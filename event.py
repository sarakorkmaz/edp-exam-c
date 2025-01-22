# event.py

from datetime import datetime

# Event class - base class for all events
class Event:
    def __init__(self, payload):
        self.timestamp = datetime.now()
        self.payload = payload


# Event types: Application Sent, Application Rejected, Application Accepted
class ApplicationSentEvent(Event):
    def __init__(self, student, university):
        super().__init__({"student": student, "university": university, "status": "Sent"})


class ApplicationRejectedEvent(Event):
    def __init__(self, student, university):
        super().__init__({"student": student, "university": university, "status": "Rejected"})


class ApplicationAcceptedEvent(Event):
    def __init__(self, student, university):
        super().__init__({"student": student, "university": university, "status": "Accepted"})
