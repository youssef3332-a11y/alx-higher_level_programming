#!/usr/bin/python3
"""i don't know what to do"""


class Node:
    """i m tring !"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if value != None:
            if not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")
        self.__next_node = value
class SinglyLinkedList:
    def __init__(self):
        self.__head = None
    def __str__(self):
        curant = self.__head
        printed = ""
        while curant != None:
            printed += str(curant.data) + "\n"
            curant = curant.next_node
        return printed
    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            curant = self.__head
            while curant:
                if curant.data <= value:
                    if curant.next_node is None:
                        curant.next_node = new
                    else:
                        if curant.next_node.data > value:
                            new.next_node = curant.next_node
                            curant.next_node = new
                curant = curant.next_node