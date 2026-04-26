
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueFullError(Exception):
    pass


class Queue:
    def __init__(self, size=5):
        self.head = None
        self.tail = None
        self.size = size
        self.current_size = 0

    def enqueue(self, data):
        if self.current_size == self.size:
            raise QueueFullError("Queue is full")

        temp = Node(data)

        if self.tail is None:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

        self.current_size += 1

    def front(self):
        if self.head is None:
            return None

        return self.head.data

    def dequeue(self):
        if self.head is None:
            return None

        temp = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.current_size -= 1

        return temp

    def is_empty(self):
        if self.head is None:
            return True

        return False

    def is_empty2(self):
        if self.current_size == 0:
            return True

        return False


myqueue = Queue()
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
myqueue.enqueue(9)
myqueue.enqueue(9)
myqueue.enqueue(9)
myqueue.dequeue()
# myqueue.dequeue()

print(myqueue.front())

print("Total number of data -> ", myqueue.current_size)
