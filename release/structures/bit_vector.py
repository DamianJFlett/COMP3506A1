"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

from structures.dynamic_array import DynamicArray


class BitVector:
    """
    A compact storage for bits that uses DynamicArray under the hood.
    Each element stores up to 64 bits, making BitVector 64 times more memory-efficient
    for storing bits than plain DynamicArray.
    """

    BITS_PER_ELEMENT = 64

    def __init__(self) -> None:
        """
        We will use the dynamic array as our data storage mechanism
        """
        self._data = DynamicArray()
        self._size = 0

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.
        """
        rep = ""
        for i in range(0,self._size):
            if not (i % self.BITS_PER_ELEMENT):
                rep += " "
            rep += str(self[i])
        return rep
    
    def __resize(self) -> None:
        self._data.append(0)

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index >= self._size:
            return None
        if index // self.BITS_PER_ELEMENT == self._size //self.BITS_PER_ELEMENT:  
            return (self._data[index // self.BITS_PER_ELEMENT] >> (((self._size-1) % self.BITS_PER_ELEMENT - index) % self.BITS_PER_ELEMENT)) & 1
        else:
            return (self._data[index // self.BITS_PER_ELEMENT] >> ((self.BITS_PER_ELEMENT -1 - index % self.BITS_PER_ELEMENT))) & 1
    
    def __getitem__(self, index: int) -> int | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int) -> None:
        """
        Set bit at the given index to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index >= self._size:
            return None
        if index // self.BITS_PER_ELEMENT == self._size //self.BITS_PER_ELEMENT: 
            self._data[index // self.BITS_PER_ELEMENT] = \
                self._data[index // self.BITS_PER_ELEMENT] | (1 << (((self._size - 1) % self.BITS_PER_ELEMENT - index) % self.BITS_PER_ELEMENT))
        else:
            self._data[index // self.BITS_PER_ELEMENT] = \
                self._data[index // self.BITS_PER_ELEMENT] | (1 << (self.BITS_PER_ELEMENT - 1 - index % self.BITS_PER_ELEMENT))

    def unset_at(self, index: int) -> None:
        """
        Set bit at the given index to 0.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index >= self._size:
            return None
        if index // self.BITS_PER_ELEMENT == self._size //self.BITS_PER_ELEMENT: 
            self._data[index // self.BITS_PER_ELEMENT] = \
                self._data[index // self.BITS_PER_ELEMENT] & ~(1 << (((self._size - 1) % self.BITS_PER_ELEMENT - index) % self.BITS_PER_ELEMENT))
        else:
            self._data[index // self.BITS_PER_ELEMENT] = \
                self._data[index // self.BITS_PER_ELEMENT] & ~(1 << ((self.BITS_PER_ELEMENT - 1 - index) % self.BITS_PER_ELEMENT))

    def __setitem__(self, index: int, state: int) -> None:
        """
        Set bit at the given index.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if state == 0:
            self.unset_at(index)
        else:
            self.set_at(index)

    def append(self, state: int) -> None:
        """
        Add a bit to the back of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if self._size % self.BITS_PER_ELEMENT == 0:
            self.__resize()
            self._data[self._size // self.BITS_PER_ELEMENT] = state
            self._size +=1
            return
        self._data[self._size // self.BITS_PER_ELEMENT] *= 2
        if state:
            self._data[self._size // self.BITS_PER_ELEMENT] += 1
        self._size += 1
    
    def prepend(self, state: Any) -> None:
        """
        Add a bit to the front of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        if self._size % self.BITS_PER_ELEMENT == 0:
            self.__resize()
        self._size += 1
        self[0] = state

    def _right_shift(self, array: list[int]) -> list[int]:
        """
        Shifts the entire array 1 bit to the right and isnerts teh start insert at the left
        """
        start = 0
        for i in range(self._data.get_size()-1, -1, -1):
            carry = array[i] & 1
            array[i] = (array[i] >> 1) | (start << (self.BITS_PER_ELEMENT -1))
            start = carry
        return array

    def pre_allocate(self, size: int) -> None:
        self._size = size
        self._data = [0] * (size // 64 + 1)

    def reverse(self) -> None:
        """
        Reverse the bit-vector.
        Time complexity for full marks: O(1)
        """
        pass

    def flip_all_bits(self) -> None:
        """
        Flip all bits in the vector.
        Time complexity for full marks: O(1)
        """
        pass

    def shift(self, dist: int) -> None:
        """
        Make a bit shift.
        If dist is positive, perform a left shift by `dist`.
        Otherwise perform a right shift by `dist`.
        Time complexity for full marks: O(N)
        """

    def rotate(self, dist: int) -> None:
        """
        Make a bit rotation.
        If dist is positive, perform a left rotation by `dist`.
        Otherwise perform a right rotation by `dist`.
        Time complexity for full marks: O(N)
        """

    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._size
    
