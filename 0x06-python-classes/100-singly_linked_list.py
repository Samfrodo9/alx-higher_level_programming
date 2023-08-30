class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == int
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = head

     def sorted_insert(self, value):
        new_node = Node(value)
        
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
