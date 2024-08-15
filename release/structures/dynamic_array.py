"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any


class DynamicArray:
    def __init__(self) -> None:
        self._size = 0
        self._capacity = 1
        self._elements = [None] * self._capacity
        self._reversed = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        rep = "[]"
        if not self._reversed: #not right, what about all the noen elements
            for (index, element) in enumerate(self._elements):
                rep += element
                if self._size != index - 1:
                    rep += ", "
                else:
                    rep += "]"
        else:
            i = self._size
            while i > 0:
                rep += self._elements[i]
                rep += ", "
                i -= 1
            rep += self._elements[i]
            rep += "]"
        return rep

    def __resize(self) -> None:
        capacity = capacity * 2

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        i = 1
        if not self._reversed:
            pass


    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int, element: Any) -> None:
        """
        Get element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        pass

    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        return self.set_at(index)

    def append(self, element: Any) -> None:
        """
        Add an element to the back of the array.
        Time complexity for full marks: O(1*) (* means amortized)
        """
        pass

    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        pass

    def reverse(self) -> None:
        """
        Reverse the array.
        Time complexity for full marks: O(1)
        """
        self._reversed = not self._reversed

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        pass

    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        pass

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        return self._size == 0

    def is_full(self) -> bool:
        """
        Boolean helper to tell us if the structure is full or not
        Time complexity for full marks: O(1)
        """
        return self._size == self._capacity

    def get_size(self) -> int:
        """
        Return the number of elements in the list
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of slots) of the list
        Time complexity for full marks: O(1)
        """
        return self._capacity

    def sort(self) -> None:
        """
        Sort elements inside _data based on < comparisons.
        Time complexity for full marks: O(NlogN)
        """
        pass
