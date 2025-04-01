from collections import deque


class Stack_Queue:
    def __init__(self):
        self.queue = deque()
        self.stack = deque()

    def stack_size(self,):
        return self.stack.__sizeof__()

    def queue_size(self,):
        return self.queue.__sizeof__()

    def is_empty_stack(self):
        return len(self.stack) == 0
