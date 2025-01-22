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