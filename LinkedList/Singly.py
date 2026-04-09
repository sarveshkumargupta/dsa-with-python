
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)

        current_head = self.head

        if current_head is None:
            self.head = new_node
            return

        while current_head.next:
            current_head = current_head.next

        current_head.next = new_node

    def print_all(self):
        current_head = self.head

        while current_head:
            print(current_head.data)
            current_head = current_head.next

    def insert_after_value(self, value, after):
        new_node = Node(value)

        current_head = self.head

        while current_head:
            if current_head.data == after:
                new_node.next = current_head.next
                current_head.next = new_node
                return

            current_head = current_head.next

    def delete_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return True

        current_head = self.head.next
        prev_head = current_head

        while current_head:
            if current_head.data == value:
                prev_head.next = current_head.next
                return True

            prev_head = current_head
            current_head = current_head.next

        return False

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        current = self.head
        next = current.next
        prev = current

        while current:
            next.next = prev

            prev = current
            current = current.next

        current.next = head


mylist = SinglyLL()

mylist.insert_at_end(2)
mylist.insert_at_end(13)
mylist.insert_at_end(4)
mylist.insert_after_value(19, 41)
# mylist.insert_at_end(5)
# mylist.delete_value(5)
# mylist.insert_at_beginning(12)


mylist.print_all()
# mylist.reverse()
# print("Reversed")
# mylist.print_all()
