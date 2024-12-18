"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

#  so we can hint Node get_next
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
    Note that any time you see `Any` in the type annotations,
    this refers to the "data" stored inside a Node.

    [V3: Note that this API was changed in the V3 spec] 
    """

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._reversed = False #flag for if list should act as reversed
        self._size = 0

    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """
        rep = "["
        if not self._reversed: #start at head if not reversed, tail otherwise
            curr = self._head
        else:
            curr = self._tail
        while curr:
            if not self._reversed:
                next_node = curr.get_next()
            else:
                next_node = curr.get_prev()
            rep += str(curr.get_data()) #add data of current node and move on in list
            if next_node:
                rep += ", "
            curr = next_node
        return rep + "]"
    

    """
    Simple Getters and Setters
    """
    
    def get_size(self) -> int:
        """
        Return the size of the list.
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_head(self) -> Any | None:
        """
        Return the data of the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if not (self._tail or self._head):
            return None
        if not self._reversed:
            return self._head.get_data()
        return self._tail.get_data()

    def set_head(self, data: Any) -> None:
        """
        Replace the leftmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if self._head and (not self._reversed):
            self._head.set_data(data)
        elif self._tail:
            self._tail.set_data(data)

    def get_tail(self) -> Any | None:
        """
        Return the data of the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if not (self._tail or self._head):
            return None
        if not self._reversed:
            return self._tail.get_data()
        return self._head.get_data()
    def set_tail(self, data: Any) -> None:
        """
        Replace the rightmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if self._tail and (not self._reversed):
            self._tail.set_data(data)
        elif self._head:
            self._head.set_data(data)
    """
    More interesting functionality now.
    """

    def insert_to_front(self, data: Any) -> None:
        """
        Insert the given data to the front of the list.
        Hint: You will need to create a Node type containing
        the given data.
        Time complexity for full marks: O(1)
        """
        if not self._reversed:
            self._insert_to_front_logical(data)
        else:
            self._insert_to_back_logical(data)
    
    #inserts to the front of the list as internally stored
    #looks as if inserting to back if reversed
    def _insert_to_front_logical(self, data: Any) -> None:
        new_head = Node(data)
        self._size +=1
        new_head.set_next(self._head)
        if self._head:
            self._head.set_prev(new_head)
        else:
            self._tail = new_head
        self._head = new_head


    #inserts to the back of the list as internally stored
    def _insert_to_back_logical(self, data: Any) -> None:
        new_tail = Node(data)
        self._size +=1
        new_tail.set_prev(self._tail)
        if self._tail:
            self._tail.set_next(new_tail)
        else:
            self._head = new_tail
        self._tail = new_tail

    def insert_to_back(self, data: Any) -> None:
        """
        Insert the given data (in a node) to the back of the list
        Time complexity for full marks: O(1)
        """
        if not self._reversed:
            self._insert_to_back_logical(data)
        else:
            self._insert_to_front_logical(data)


    def remove_from_front(self) -> Any | None:
        """
        Remove the front node, and return the data it holds.
        Time complexity for full marks: O(1)
        """

        if self._reversed:
            return self._remove_from_back_logical()
        else:
            return self._remove_from_front_logical()

    def remove_from_back(self) -> Any | None:
        """
        Remove the back node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        if self._reversed:
            return self._remove_from_front_logical()
        else:
            return self._remove_from_back_logical()

    def _remove_from_front_logical(self) -> Any:
        if not self._head:
            return None
        self._size -= 1
        removed = self._head
        if not self._head.get_next():
            self._head = None
            self._tail = None
            return removed.get_data()
        else:
            self._head = removed.get_next()
            self._head.set_prev(None)
            return removed.get_data()

        

    def _remove_from_back_logical(self) -> Any:
        if not self._tail:
            return None
        self._size -= 1
        removed = self._tail
        if not self._tail.get_prev():
            self._head = None
            self._tail = None
            return removed.get_data()
        else:
            self._tail = removed.get_prev()
            self._tail.set_next(None)
            return removed.get_data()


    def find_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list and returns True
        if a match is found; False otherwise.
        Time complexity for full marks: O(N)
        """
        curr = self._head
        while curr:
            if curr.get_data() == elem:
                return True
            else:
                curr = curr.get_next()
        return False

    def find_and_remove_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list; if a match is
        found, this node is removed from the linked list, and True is returned.
        False is returned if no match is found.
        Time complexity for full marks: O(N)
        """
        curr = self._head
        while curr:
            if curr.get_data() != elem:
                curr = curr.get_next()
                continue
            elif not (curr.get_next() or curr.get_prev()):
                self._head = None
                self._tail = None
                self._size -=1
                return True
            elif (curr.get_next() and (not curr.get_prev())):
                self._head = curr.get_next()
                curr.get_next().set_prev(None)
                self._size -=1
                return True
            elif ((not curr.get_next()) and curr.get_prev()):
                self._tail = curr.get_prev()
                curr.get_prev().set_next(None)
                self._size -=1
                return True
            else:
                curr.get_prev().set_next(curr.get_next())
                curr.get_next().set_prev(curr.get_prev())
                self._size -=1
                return True
        return False

    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """
        self._reversed = not self._reversed
