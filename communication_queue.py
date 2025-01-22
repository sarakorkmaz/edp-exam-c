# communication_queue.py

import queue

class CommunicationQueue:
    def __init__(self):
        self._queue = queue.Queue()

    def put(self, event):
        """Put an event in the queue."""
        self._queue.put(event)

    def get(self):
        """Get the next event from the queue."""
        return self._queue.get()

    def empty(self):
        """Check if the queue is empty."""
        return self._queue.empty()

    def size(self):
        """Get the size of the queue."""
        return self._queue.qsize()
