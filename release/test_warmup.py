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

from warmup.warmup import * 

def test_main_character():
    """
    A simple set of tests for the main character problem.
    This is not marked and is just here for you to test your code.
    """
    print("main_character([1,2,3,4,5]) = ", main_character([1,2,3,4,5]))
    print("main_character([1,2,3,4,4]) = ", main_character([1,2,3,4,4]))
    print("main_character([1,2,2,4,4]) = ", main_character([1,2,2,4,4]))
    print("main_character([7, 1, 2, 7]) = ", main_character([7, 1, 2, 7]))
    my_list = [1, 2, 5, 19, 29, 80, 70]
    my_list.append(2**32)
    print("main_character(garbage) = ", main_character(my_list))
    print("main_character([1,2,1,4,4,4]) = ", main_character([1,2,1,4,4,4]))
    list2 = []
    for i in range(10000):
        list2.append(i**2)
    list2.append(2**32)
    print("finished")
    print("main charcter big list = ", main_character(list2))

def test_missing_odds():
    """
    A simple set of tests for the missing odds problem.
    This is not marked and is just here for you to test your code.
    """
    print("missing_odds([1, 2]) = ",  missing_odds([1, 2]))
    print("missing_odds([1, 3]) = ", missing_odds([1,3]))
    print("missing_odds([1,4]) =", missing_odds([1,4]))
    print("missing_odds([4,1]) = ", missing_odds([4,1]))
    print("missing_odds([4,1,8,5]) = ", missing_odds([4,1,8,5]))
    my_list = []
    for i in range(1, 300000):
        my_list.append(i)
    print("missing odds garbage", missing_odds(my_list))
    print("missing odds([1,3,5,7,11,15]) = ",missing_odds([1,3,5,7,11,15]))
def test_k_cool():
    """
    A simple set of tests for the k cool problem.
    This is not marked and is just here for you to test your code.
    """
    print("k_cool(3, 10) = ", k_cool(3, 10))
    print("k_cool(10**30, 10**90000) = ", k_cool(128, 5000))
def test_number_game():
    """
    A simple set of tests for the number game problem.
    This is not marked and is just here for you to test your code.
    """
    print("number_game([5, 2, 7,3]) = ", number_game([5,2,7,3]))
    print("number_game([1,8 ,5, -9,2]) = ", number_game([1,8,5,-9,2]))
    print(number_game([1,5,4,2,1,3,5,32,3,9,102,1,-2,4]))

def test_road_illumination():
    """
    A simple set of tests for the road illumination problem.
    This is not marked and is just here for you to test your code.
    """
    print("road_illumination(15, [15, 5, 3, 7, 9, 14, 0]) = ",road_illumination(15, [15, 5, 3, 7, 9, 14, 0]))
    print("road_illumination(5, [2,5]) = ",road_illumination(5,[2,5]))

# The actual program we're running here
if __name__ == "__main__":
    # Get and parse the command line arguments
    parser = argparse.ArgumentParser(description="COMP3506/7505 Assignment One: Testing Warmup Problems")

    parser.add_argument("--character", action="store_true", help="Test your main character sol.")
    parser.add_argument("--odds", action="store_true", help="Test your missing odds sol.")
    parser.add_argument("--kcool", action="store_true", help="Test your k-cool sol.")
    parser.add_argument("--numbergame", action="store_true", help="Test your number game sol.")
    parser.add_argument("--road", action="store_true", help="Test your road illumination sol.")
    parser.add_argument("--seed", type=int, default='42', help="Seed the PRNG.")
    args = parser.parse_args()

    # No arguments passed
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    # Seed the PRNG in case you are using randomness
    random.seed(args.seed)

    # Now check/run the selected algorithm
    if args.character:
        test_main_character()

    if args.odds:
        test_missing_odds()

    if args.kcool:
        test_k_cool()

    if args.numbergame:
        test_number_game()

    if args.road:
        test_road_illumination()

