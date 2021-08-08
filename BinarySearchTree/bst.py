

class BinarySearchTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value == self.value:
            return

        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def search(self, value):
        if value == self.value:
            return True

        if value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def in_order(self):
        values = []
        if self.left:
            values += self.left.in_order()

        values.append(self.value)

        if self.right:
            values += self.right.in_order()

        return values

    def pre_order(self):
        values = [self.value]

        if self.left:
            values += self.left.pre_order()

        if self.right:
            values += self.right.pre_order()

        return values

    def post_order(self):
        values = []

        if self.left:
            values += self.left.pre_order()

        if self.right:
            values += self.right.post_order()

        values.append(self.value)

        return values


obj1 = BinarySearchTree(10)

obj1.insert(5)
obj1.insert(8)
obj1.insert(2)
obj1.insert(12)
obj1.insert(3)
obj1.insert(9)

print(obj1.search(12))

print(obj1.pre_order())
print(obj1.in_order())
print(obj1.post_order())
