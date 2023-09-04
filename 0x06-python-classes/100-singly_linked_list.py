#!/usr/bin/python3

"""A module that has a Node and List defined"""


class Node:
    '''This class defines a node'''
    def __init__(self, data, next_node=None):
        """A function that initializes a list"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = None

    @property
    def data(self):
        """retrieves the value for data"""
        return self.__data

    @data.setter
    def data(self, value):
        '''Set the value for data'''
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        '''retrieve the value for next node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''set the value for next node'''
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    '''A class that defines a singly linked list'''
    def __init__(self):
        '''initializes the head of the list'''
        self.__head = None

    def sorted_insert(self, value):
        '''sorts the list in increasing order'''
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
