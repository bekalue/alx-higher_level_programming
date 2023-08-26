#!/usr/bin/python3
'''A module for working with singly linked lists.
'''


class Node:
    '''Represents a node in a singly linked list.
    '''
    def __init__(self, data, next_node=None):
        '''Initializes a Node with a given data and next link.

        Args:
            data (int): The data of the Node.
            next_node (Node): The Node next to this Node.
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Retrieves the data of this Node.

        Returns:
            int: The data of this Node.
        '''
        return self.__data

    @property
    def next_node(self):
        '''Retrieves the Node next to this Node.

        Returns:
            Node: The Node next to this Node.
        '''
        return self.__next_node

    @data.setter
    def data(self, value):
        '''Updates the data of this Node.

        Args:
            value (int): The new data of this Node.
        '''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        '''Updates the next node of this Node.

        Args:
            value (Node): The new node next to  this Node.
        '''
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    '''Represents a singly linked list.
    '''
    def __init__(self):
        '''Initializes a singly linked list.'''
        self.__head = None

    def sorted_insert(self, value):
        '''Inserts a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value (int): The data of the Node to be inserted into the list.
        '''
        if not isinstance(value, int) or value is None:
            raise TypeError('value must be an integer')
        else:
            if self.__head is None or self.__head.data >= value:
                new_node = Node(value, self.__head)
                self.__head = new_node
            else:
                node_ptr = self.__head
                prev_ptr = None
                while node_ptr is not None and value > node_ptr.data:
                    prev_ptr = node_ptr
                    node_ptr = node_ptr.next_node
                new_node = Node(value, node_ptr)
                prev_ptr.next_node = new_node

    def __str__(self):
        '''Returns a string representation of this singly linked list.

        Returns:
            str: A string representation of this singly linked list.
        '''
        node_ptr = self.__head
        res = []
        while node_ptr is not None:
            res.append(str(node_ptr.data))
            node_ptr = node_ptr.next_node
        return '' if len(res) == 0 else '\n'.join(res)
