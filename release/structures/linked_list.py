"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

# so we can hint Node get_next
from __future__ import annotations

from typing import Any


class Node:
    """
    A simple type to hold data and a next pointer
    """

    def __init__(self, data: Any) -> None:
        self._data = data  # This is the payload data of the node
        self._next = None  # This is the "next" pointer to the next Node
        self._prev = None  # This is the "previous" pointer to the previous Node

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data

    def set_next(self, node: Node) -> None:
        self._next = node

    def get_next(self) -> Node | None:
        return self._next

    def set_prev(self, node: Node) -> None:
        self._prev = node

    def get_prev(self) -> Node | None:
        return self._prev


class DoublyLinkedList:
    """
    Your doubly linked list code goes here.
    """

    def __init__(self) -> None:
        # You probably need to track some data here...
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """
        current_node = self.head
        output = "["
        while current_node:
            output += current_node.get_data()
            output += ", "
            current_node = current_node.get_next()
        output = output[:-2] + "]"
        return output

        

    """
    Simple Getters and Setters below
    """

    def get_size(self) -> int:
        """
        Return the size of the list.
        Time complexity for full marks: O(1)
        """
        return self.size

    def get_head(self) -> Node | None:
        """
        Return the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        return self.head

    def set_head(self, node: Node) -> None:
        """
        Replace the leftmost node in the list.
        Time complexity for full marks: O(1)
        """
        if not self.head:
            self.size+=1
            self.tail = node
        self.head = node

    def get_tail(self) -> Node | None:
        """
        Return the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        return self.tail

    def set_tail(self, node: Node) -> None:
        """
        Replace the rightmost node in the list.
        Time complexity for full marks: O(1)
        """
        if not self.tail:
            self.size+=1
            self.head = node
        self.tail = node

    """
    More interesting functionality now.
    """

    def insert_to_front(self, node: Node) -> None:
        """
        Insert a node to the front of the list
        Time complexity for full marks: O(1)
        """
        if self.head:
            node.set_next(self.head)
            node.get_next().set_prev(node)
        else:
            node.set_next(None)
            self.tail = node
        node.set_prev(None)
        self.head = node
        self.size+=1

    def insert_to_back(self, node: Node) -> None:
        """
        Insert a node to the back of the list
        Time complexity for full marks: O(1)
        """
        if self.tail:
            node.set_prev(self.tail)
            node.get_prev().set_next(node)
        else:
            node.set_prev(None)
            self.head = node
        node.set_next(None)
        self.tail = node
        self.size+=1

    def remove_from_front(self) -> Node | None:
        """
        Remove and return the front element
        Time complexity for full marks: O(1)
        """
        self.head = self.head.get_next()
        self.head.set_prev(None)
        size -=1

    def remove_from_back(self) -> Node | None:
        """
        Remove and return the back element
        Time complexity for full marks: O(1)
        """
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)
        self.size -=1

    def find_element(self, elem: Any) -> Any | None:
        """
        Looks at the data inside each node of the list and returns the
        node if it matches the input elem; returns None otherwise
        Time complexity for full marks: O(N)
        """
        current_node = self.head
        while current_node:
            if (current_node.get_data() == elem):
                return current_node
            current_node = current_node.get_next()
        return None
    
    def find_and_remove_element(self, elem: Any) -> Any | None:
        """
        Finds, removes, and returns the first instance of elem
        (based on the node data) or returns None if the element is not found.
        Time complexity for full marks: O(N)
        """
        current_node = self.head
        while current_node:
            if (current_node.get_data() == elem):
                if (current_node.get_prev() and current_node.get_next()):
                    current_node.get_prev().set_next(current_node.get_next())
                    current_node.get_next().set_prev(current_node.get_prev())
                elif current_node.get_prev():
                    self.set_tail(current_node.get_prev())
                    current_node.get_prev().set_next(None)
                elif current_node.get_next():
                    self.set_head(current_node.get_next())
                    current_node.get_next().set_prev(None)
                self.size-=1
                return current_node
            current_node = current_node.get_next()
        return None

    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """
        current_node = self.get_head()
        while current_node:
            new_next = current_node.get_prev()
            new_prev = current_node.get_next()
            current_node.set_next(new_next)
            current_node.set_prev(new_prev)
            current_node = current_node.get_prev()
        new_head = self.get_tail()
        new_tail = self.get_head()
        self.set_tail(new_tail)
        self.set_head(new_head)


