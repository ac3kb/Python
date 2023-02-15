class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Doublylinkedlist:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 1


    def append(self, value):
        self.add_node = Node(value)
        if self.head is None:
            self.head = self.add_node
            self.tail = self.add_node
        else:
            self.tail.next = self.add_node
            self.add_node.prev = self.tail
            self.tail = self.add_node
            self.length += 1
        return True


    def pop(self):
        if self.head is None:
            return None
        else:
            self.temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.temp.prev = None
            self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

    def moreReadablePop(self):
        if self.length == 0:
            return None
        self.temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.temp.prev = None
        self.length -= 1
        return self.temp



    def prepend(self, value):
        self.prepend_node = Node(value)
        if self.head is None:
            self.head = self.prepend_node
            self.tail = self.prepend_node
        else:
            self.prepend_node.next = self.head
            self.head.prev = self.prepend_node
            self.head = self.prepend_node
        self.length += 1
        return True


    def pop_first(self):
        if self.length == 0:
            return None
        self.temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            self.temp.next = None
        self.length -= 1
        return self.temp


    def insert(self, index, value):
        self.insert_node = Node(value)
        self.temp = self.get(index)


