"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov

WARMUP PROBLEMS

 Each problem will be assessed on three sets of tests:

1. "It works":
       Basic inputs and outputs, including the ones peovided as examples, with generous time and memory restrictions.
       Large inputs will not be tested here.
       The most straightforward approach will likely fit into these restrictions.

2. "Exhaustive":
       Extensive testing on a wide range of inputs and outputs with tight time and memory restrictions.
       These tests won't accept brute force solutions, you'll have to apply some algorithms and optimisations.

 3. "Welcome to COMP3506":
       Extensive testing with the tightest possible time and memory restrictions
       leaving no room for redundant operations.
       Every possible corner case will be assessed here as well.

There will be hidden tests in each category that will be published only after the assignment deadline.
"""

"""
You may wish to import your data structures to help you with some of the
problems. Or maybe not. We did it for you just in case.
"""
from structures.bit_vector import BitVector
from structures.dynamic_array import DynamicArray
from structures.linked_list import DoublyLinkedList, Node
from random import randint

def main_character(instring: list[int]) -> int:
    """
    @instring@ is an array of integers in the range [0, 2^{32}-1].
    Return the first position a repeat integer is encountered, or -1 if
    there are no repeated ints.

    Limitations:
        "It works":
            @instring@ may contain up to 10'000 elements.

        "Exhaustive":
            @instring@ may contain up to 300'000 elements.

        "Welcome to COMP3506":
            @instring@ may contain up to 5'000'000 elements.

    Examples:
    main_character([1, 2, 3, 4, 5]) == -1
    main_character([1, 2, 1, 4, 4, 4]) == 2
    main_character([7, 1, 2, 7]) == 3
    main_character([60000, 120000, 654321, 999, 1337, 133731337]) == -1
    """
    seen = BitVector()
    max = 0
    for i in instring:
        if i > max:
            max = i
        seen.pre_allocate(max+1)
    for (index, i) in enumerate(instring):
        if seen[i]:
            return index
        seen.set_at(i)
    return -1

def missing_odds(inputs: list[int]) -> int:
    """
    @inputs@ is an unordered array of distinct integers.
    If @a@ is the smallest number in the array and @b@ is the biggest,
    return the sum of odd numbers in the interval [a, b] that are not present in @inputs@
    If there are no such numbers, return 0.

    Limitations:
        "It works":
            @inputs@ may contain up to 10'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^4
        "Exhaustive":
            @inputs@ may contain up to 300'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^6
        "Welcome to COMP3506":
            @inputs@ may contain up to 5'000'000 elements.
            Each element is in range 0 <= inputs[i] <= 10^16

    Examples:
    missing_odds([1, 2]) == 0
    missing_odds([1, 3]) == 0
    missing_odds([1, 4]) == 3
    missing_odds([4, 1]) == 3
    missing_odds([4, 1, 8, 5]) == 10    # 3 and 7 are missing
    """
    running_total = 0 #  sum of odd numbers present in (min, max)
    min = inputs[0]
    max = inputs[0]
    for i in inputs:
        if i < min:
            min = i
        if i > max:
            max = i
        if i % 2:
            running_total += i
    if min % 2:
        running_total -= min
    if max % 2:
        running_total -= max
    size = _count_odds(min, max) 
    if min % 2 and max % 2:
        return (size * (min + max)) // 2 - running_total
    elif  not (min % 2 or max % 2):
        return (size * (min + max)) // 2 - running_total
    elif min % 2 and not (max % 2):
        return (size * (min + max+1)) // 2 - running_total
    else:
        return (size * (min + max-1)) // 2 - running_total
        
def _count_odds(min: int, max: int) -> int:
    """
    Counts odd numbers in [a,b] exclusive
    """
    if min % 2 and max % 2:
        return (max - min) // 2 - 1 
    else:
        return (max - min) // 2 

def k_cool(k: int, n: int) -> int:
    """
    Return the n-th largest k-cool number for the given @n@ and @k@.
    The result can be large, so return the remainder of division of the result
    by 10^16 + 61 (this constant is provided).

    Limitations:
        "It works":
            2 <= k <= 128
            1 <= n <= 10000
        "Exhaustive":
            2 <= k <= 10^16
            1 <= n <= 10^100     (yes, that's ten to the power of one hundred)
        "Welcome to COMP3506":
            2 <= k <= 10^42
            1 <= n <= 10^100000  (yes, that's ten to the power of one hundred thousand)

    Examples:
    k_cool(2, 1) == 1                     # The first 2-cool number is 2^0 = 1
    k_cool(2, 3) == 2                     # The third 2-cool number is 2^1 + 2^0 = 3
    k_cool(3, 5) == 10                    # The fifth 3-cool number is 3^2 + 3^0 = 10
    k_cool(10, 42) == 101010
    k_cool(128, 5000) == 9826529652304384 # The actual result is larger than 10^16 + 61,
                                          # so k_cool returns the remainder of division by 10^16 + 61
    """
    #looks like these map onto binary numbers
    MODULUS = 10**16 + 61

    answer = 0 
    current_term = 1
    for i in range(0, n.bit_length()):
        if (n >> i) & 1:
            answer += current_term % MODULUS #  modulus at every step so adding and multiplying
        current_term = (current_term % MODULUS) * k #  operations dont get out of hand with many digits
    return answer % MODULUS



def number_game(numbers: list[int]) -> tuple[str, int]:
    """
    @numbers@ is an unordered array of integers. The array is guaranteed to be of even length.
    Return a tuple consisting of the winner's name and the winner's score assuming that both play optimally.
    "Optimally" means that each player makes moves that maximise their chance of winning
    and minimise opponent's chance of winning.
    You are ALLOWED to use a tuple in your return here, like: return (x, y)
    Possible string values are "Alice", "Bob", and "Tie"

    Limitations:
        "It works":
            @numbers@ may contain up to 10'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^6
        "Exhaustive":
            @numbers@ may contain up to 100'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^16
        "Welcome to COMP3506":
            @numbers@ may contain up to 300'000 elements.
            Each element is in range 0 <= numbers[i] <= 10^16

    Examples:
    number_game([5, 2, 7, 3]) == ("Bob", 5)
    number_game([3, 2, 1, 0]) == ("Tie", 0)
    number_game([2, 2, 2, 2]) == ("Alice", 4)

    For the second example, if Alice picks 2 to increase her score, Bob will pick 3 and win. Alice does not want that.
    The same happens if she picks 1 or 0, but this time she won't even increase her score.
    The only scenario when Bob does not win immediately is if Alice picks 3.
    Then, Bob faces the same choice:
    pick 1 to increase his score knowing that Alice will pick 2 and win, or pick 2 himself.
    The same happens on the next move.
    So, nobody picks any numbers to increase their score, which results in a Tie with both players having scores of 0.
    """

    # bob and alice just pick the biggest number they can see, bigger number = better person
    _reverse_sort(numbers, 0, len(numbers) - 1)
    bob_score = 0
    alice_score = 0
    print(numbers)
    for (index, i) in enumerate(numbers): 
        if not (index % 2) and not (i % 2):
            alice_score += i
        elif (index % 2) and (i % 2):
            bob_score += i
    if alice_score > bob_score:
        return ("Alice", alice_score)
    elif bob_score > alice_score:
        return ("Bob",bob_score)
    else:
        return("Tie",bob_score)


def _reverse_sort(inlist: list[int], left:int, right: int) -> list[int]:
    """
    Sorts the list inlist into descending order recursively and in-place via quicksort
    """
    if left >= right:
        return
    pivot = randint(left, right)
    h = _reverse_partition(inlist, left, right, pivot)
    _reverse_sort(inlist, left, h -1)
    _reverse_sort(inlist, h + 1, right)

def _reverse_partition(inlist: list[int], left: int, right: int, pivot: int) -> int:
    inlist[pivot], inlist[left] = inlist[left], inlist[pivot]
    at_pivot = inlist[left] # data at the pivot 
    left_index = left + 1 # pointer to left index, so we dont change left, to be used later
    for i in range(left + 1, right + 1):
        if inlist[i] > at_pivot:
            inlist[i], inlist[left_index] = inlist[left_index], inlist[i] # swap if we found on wrong side of pointer
            left_index += 1
    inlist[left], inlist[left_index - 1] = inlist[left_index - 1], inlist[left]
    return left_index - 1

def road_illumination(road_length: int, poles: list[int]) -> float:
    """
    @poles@ is an unordered array of integers.
    Return a single floating point number representing the smallest possible radius of illumination
    required to illuminate the whole road.
    Floating point numbers have limited precision. Your answer will be accepted
    if the relative or absolute error does not exceed 10^(-6),
    i.e. |your_ans - true_ans| <= 0.000001 OR |your_ans - true_ans|/true_ans <= 0.000001

    Limitations:
        "It works":
            @poles@ may contain up to 10'000 elements.
            0 <= @road_length@ <= 10^6
            Each element is in range 0 <= poles[i] <= 10^6
        "Exhaustive":
            @poles@ may contain up to 100'000 elements.
            0 <= @road_length@ <= 10^16
            Each element is in range 0 <= poles[i] <= 10^16
        "Welcome to COMP3506":
            @poles@ may contain up to 300'000 elements.
            0 <= @road_length@ <= 10^16
            Each element is in range 0 <= poles[i] <= 10^16

    Examples:
    road_illumination(15, [15, 5, 3, 7, 9, 14, 0]) == 2.5
    road_illumination(5, [2, 5]) == 2.0
    """

    #consecutive pairs in the list distance x away need x/2 minimum to illuminate
    #maybe ??
    _sort(poles, 0, len(poles) -1)
    if poles[0] >= road_length - poles[len(poles)-1]:
        current_rad = 2 * poles[0]
    else:
        current_rad = 2 * (road_length - poles[len(poles) - 1])
    for index in range(0,len(poles)-2):
        print(current_rad)
        diff = abs(poles[index] - poles[index + 1])
        if diff > current_rad:
            current_rad = diff
    return current_rad / 2



#  how op is not being marked on style i can just copy 20 lines of code
def _sort(inlist: list[int], left:int, right: int) -> list[int]:
    """
    Sorts the list inlist into descending order recursively and in-place via quicksort
    """
    if left >= right:
        return
    pivot = randint(left, right)
    h = _partition(inlist, left, right, pivot)
    _sort(inlist, left, h -1)
    _sort(inlist, h + 1, right)

def _partition(inlist: list[int], left: int, right: int, pivot: int) -> int:
    inlist[pivot], inlist[left] = inlist[left], inlist[pivot]
    at_pivot = inlist[left] # data at the pivot 
    left_index = left + 1 # pointer to left index, so we dont change left, to be used later
    for i in range(left + 1, right + 1):
        if inlist[i] < at_pivot:
            inlist[i], inlist[left_index] = inlist[left_index], inlist[i] # swap if we found on wrong side of pointer
            left_index += 1
    inlist[left], inlist[left_index - 1] = inlist[left_index - 1], inlist[left]
    return left_index - 1

