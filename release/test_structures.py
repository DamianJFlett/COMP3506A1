"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

NOTE: This file is not used for assessment. It is just a driver program for
you to write your own test cases and execute them against your data structures.
"""

# Import helper libraries
import random
import sys
import time
import argparse

# Import our data structures
from structures.linked_list import Node, DoublyLinkedList
from structures.dynamic_array import DynamicArray 
from structures.bit_vector import BitVector

def test_linked_list():
    """
    A simple set of tests for the linked list implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Linked List Tests ====")

    # Consider expanding these tests into your own methods instead of
    # just doing a bunch of stuff here - this is just to get you started
    
    # OK, let's add some strings to a list
    my_list = DoublyLinkedList()
    assert(my_list.get_size() == 0)

    my_list.insert_to_front("hello")
    print(my_list.get_head(), "head")
    print(my_list.get_tail(), "tail")
    my_list.insert_to_back("algorithms")
    print(my_list.get_head(), "head")
    print(my_list.get_tail(), "tail")

    # Have a look - we can do this due to overriding __str__ in the class
    print(str(my_list), "Size is", my_list.get_size()) 
    print(my_list.get_head(), "head")
    print(my_list.get_tail(), "tail")



    # Now lets try to find a node
    elem = my_list.find_element("algorithms")
    if elem:
        print("algorithms is indeed in the list")
    else:
        print("algorithms not found!")

    # And try to delete one
    elem = my_list.find_and_remove_element("1337")
    if elem:
        print ("Hang on, that wasn't in the list!")
    else:
        print ("No such element 1337")

    # And try to delete another one
    elem = my_list.find_and_remove_element("hello")
    if elem:
        print ("Deleted something")
    else:
        print ("Didn't find element = hello")

    # Have another look
    print(str(my_list))

    # OK, now check size
    assert(my_list.get_size() == 1)


    #some more tests for larger sizes
    new_list = DoublyLinkedList()
    new_list.insert_to_front("1")
    new_list.insert_to_back("2")
    new_list.insert_to_front("0")
    new_list.insert_to_back("3")
    new_list.insert_to_back("4")
    print(str(new_list), "size = ", new_list.get_size())
    print("head and tail are", new_list.get_head(), new_list.get_tail())
    new_list.remove_from_front()
    print("head and tail are", new_list.get_head(), new_list.get_tail())
    new_list.remove_from_back()
    print("head and tail are", new_list.get_head(), new_list.get_tail())
    print(str(new_list), "Size is", new_list.get_size())
    new_list.reverse()
    print(str(new_list),  "now reversed")
    new_list.insert_to_front("4")
    new_list.insert_to_back("0")
    print(str(new_list), "size is now", new_list.get_size())
    new_list.remove_from_front()
    print("element removed from front, list is not", new_list, "size is", new_list.get_size())
    new_list.remove_from_front()
    print("element removed from front, list is not", new_list, "size is", new_list.get_size())
    new_list.remove_from_back()
    print("element removed from back, list is not", new_list, "size is", new_list.get_size())
    new_list.remove_from_back()
    print("element removed from back, list is not", new_list, "size is", new_list.get_size())
    new_list.remove_from_front()
    print("3head tail is", new_list.get_head(), new_list.get_tail())
    print("element removed from front, list is not", new_list, "size is", new_list.get_size())
    new_list.remove_from_front()
    new_list.remove_from_back()
    print(new_list)
    print(new_list.get_size())
    new_list.reverse()
    new_list.reverse()
    print(str(new_list))
    new_list.insert_to_front("7")
    print("inserted at front, head tail is", new_list.get_head(), new_list.get_tail(), "list is",str(new_list))
    print(new_list._reversed)
    new_list.insert_to_front("6")
    print("inserted at front, head tail is", new_list.get_head(), new_list.get_tail(), "list is",str(new_list))
    new_list.insert_to_front("5")
    print("inserted at front, head tail is", new_list.get_head(), new_list.get_tail(), "list is",str(new_list))
    new_list.insert_to_front("4")
    print("inserted at front, head tail is", new_list.get_head(), new_list.get_tail(), "list is",str(new_list))
    new_list.insert_to_front("3")
    print("inserted at front, head tail is", new_list.get_head(), new_list.get_tail(), "list is",str(new_list))
    new_list.insert_to_front("2")
    print("inserted at front, head tail is", new_list.get_head(), new_list.get_tail(), "list is",str(new_list))
    new_list.insert_to_front("1")
    print("inserted at front, head tail is", new_list.get_head(), new_list.get_tail(), "list is",str(new_list))
    new_list.insert_to_front("0")
    print("inserted at front, head tail is", new_list.get_head(), new_list.get_tail(), "list is",str(new_list))
    print(str(new_list))
    print("head tail is", new_list._head, new_list._tail)
    print(new_list.find_and_remove_element("3"))
    print(str(new_list), "size is", new_list.get_size())
    new_list.find_and_remove_element("0")
    print(str(new_list), "size is", new_list.get_size())
    new_list.find_and_remove_element("1")
    print(str(new_list), "size is", new_list.get_size())
    new_list.find_and_remove_element("2")
    print(str(new_list), "size is", new_list.get_size())
    new_list.find_and_remove_element("4")
    new_list.find_and_remove_element("5")
    new_list.find_and_remove_element("6")
    new_list.find_and_remove_element("7")
    new_list.find_and_remove_element("8")
    new_list.find_and_remove_element("7")
    print("everything removed now", str(new_list), "size is", new_list.get_size())
    new_list.find_and_remove_element("1")
    
    new_list.reverse()
    print(str(new_list), "size is", new_list.get_size())






def test_dynamic_array():
    """
    A simple set of tests for the dynamic array implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Dynamic Array Tests ====")

def test_bitvector():
    """
    A simple set of tests for the bit vector implementation.
    This is not marked and is just here for you to test your code.
    """
    print ("==== Executing Bit Vector Tests ====")



# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description="COMP3506/7505 Assignment One: Testing Data Structures")

    parser.add_argument("--linkedlist", action="store_true", help="Test your linked list.")
    parser.add_argument("--dynamicarray", action="store_true", help="Test your dynamic array.")
    parser.add_argument("--bitvector", action="store_true", help="Test your bit vector.")
    parser.add_argument("--seed", type=int, default='42', help="Seed the PRNG.")
    
    args = parser.parse_args()

    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # Seed the PRNG in case you are using randomness
    random.seed(args.seed)

    # Now check/run the selected algorithm
    if args.linkedlist:
        test_linked_list()

    if args.dynamicarray:
        test_dynamic_array()

    if args.bitvector:
        test_bitvector()

