"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any
from random import randint

class DynamicArray:
    def __init__(self) -> None:
        self._size = 0
        self._capacity = 4 # so that always divisible by 4
        self._elements = [None] * self._capacity
        self._reversed = False
        self._first = None #first and last indexes that are full within the dumb array
        self._last = None 

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        rep = "[" 
        i = 0
        while i < self._size -1:
            rep += str(self[i])
            rep += ", "
            i += 1
        rep += str(self[self._size - 1])
        rep += "]"
        return rep

    def __resize(self) -> None:
        self._capacity = self._capacity * 2
        new_elements = [None] * self._capacity
        for i in range(self._first, self._last + 1): #self._last - self._first + 1 = self._size operations 
            new_elements[i + self._capacity // 4] = self._elements[i]
        self._first = self._first + self._capacity // 4
        self._last = self._last + self._capacity // 4
        self._elements = new_elements
        

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if (index >= self._size) or (index < 0):
            return
        if not self._reversed:
            return self._elements[self._first + index]
        else:
            return self._elements[self._last - index]


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
        if (index >= self._size) or (index < 0):
            return
        if not self._reversed:
            self._elements[index + self._first] = element
        else:
            self._elements[self._last - index] = element

    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        return self.set_at(index, element)

    def append(self, element: Any) -> None:
        """
        Add an element to the back of the array.
        Time complexity for full marks: O(1*) (* means amortized)
        """
        self._size += 1
        if self._reversed:
            self._prepend_logical(element)
        else:
            self._append_logical(element)

    def _prepend_logical(self, element: Any) -> None:
        if self._first == None:
            self._elements[0] = element
            self._first = 0
            self._last = 0
            return
        if self.is_full() or self._first - 1 <= 0:
            self.__resize()
        self._elements[self._first - 1] = element
        self._first -= 1

    def _append_logical(self, element: Any) -> None:
        if self._last == None:
            self._elements[0] = element
            self._first = 0
            self._last = 0
            return
        if self.is_full() or self._last + 1 >= self._capacity:
            self.__resize()
        self._elements[self._last + 1] = element
        self._last += 1

    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        self._size += 1
        if self._reversed:
            self._append_logical(element)
        else:
            self._prepend_logical(element)

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
        i = 0
        while i <= self._size:
            if self[i] == element:
                self.remove_at(i)
                return
            i += 1

    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        if (index >= self._size) or (index < 0):
            return
        removed = self[index]
        if not self._reversed:
            i = index
            while i < self._size -1:
                self[i] = self[i+1]
                i += 1
        else:
            i = index
            while i > 0:
                self[i] = self[i-1]
                i -= 1
        self._last -= 1
        self._size -= 1
        return removed
                


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
        #do without copying to a new array to save space? necessary?
        self._in_place_quick_sort(0, self._size - 1)

    def _in_place_quick_sort(self, left:int, right: int) -> list[int]:
        """
        Sorts the list inlist into ascending order recursively and in-place via quicksort.
        Initially hard to do in place, then done for alice and bob's game, and adapted for dynamic list. 
        """
        if left >= right:
            return
        pivot = randint(left, right)
        h = self._partition(left, right, pivot)
        self._in_place_quick_sort(left, h -1) 
        self._in_place_quick_sort(h + 1, right)

    def _partition(self: list[int], left: int, right: int, pivot: int) -> int:
        self[pivot], self[left] = self[left], self[pivot] # put pivot at left of array
        at_pivot = self[left] # the data at the pivot
        left_index = left + 1 # current pointer, so we can not modify left to use it later
        for i in range(left + 1, right + 1):
            if self[i] < at_pivot:
                self[i], self[left_index] = self[left_index], self[i] # if on the wrong side of pivot, swap
                left_index += 1
        self[left], self[left_index - 1] = self[left_index - 1], self[left]
        return left_index - 1



