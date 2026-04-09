
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def pop(self):
        if self.is_empty():
            return None

        popped_data = self.head
        self.head = self.head.next

        return popped_data

    def peek(self):
        return self.head.data if self.head else None

    def is_empty(self):
        return None if self.head else True


my_stack = Stack()

print(my_stack.is_empty())

my_stack.push(2)
my_stack.push(5)
my_stack.push(3)
my_stack.push(7)

print(my_stack.peek())

my_stack.pop()

print(my_stack.peek())

print(my_stack.is_empty())

