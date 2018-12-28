## Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. O(n2). The second function should be linear O(n)
import time
from random import randrange

def find_min_value_1(a_list):
    """ Finds the minimum value in a given list using the O(n^2)
        Uses Two nested loops
    """
    overall_min = a_list[0]
    for i in a_list:
        is_smallest = True
        for j in a_list:
            if i > j:
                is_smallest = False
        if is_smallest:
            overall_min = i
    return overall_min


def find_min_value_2(a_list):
    """ Finds the minimum value in a  given list using linear approach
        Uses Linear approach
    """
    # Checks number against the list to see if it's the smallest or not
    min_so_far = a_list[0]
    for i in a_list:
         if i < min_so_far:
             min_so_far = i
    return min_so_far

print(find_min_value_1([2,5,1,7,9,9,5,2,1,9,0,3,3,-9]))
print(find_min_value_2([9,4,2,-5,-1,6,-2,-8,8,1,8,0,-767]))


# Checks the speed of the first approach. Kind of slow and takes a while to execute
for list_size in range(1000,10001, 1000):
    a_list = [randrange(100000) for x in range(list_size)]
    start_time = time.time()
    print(find_min_value(a_list))
    end_time = time.time()
    print("Size: %d time: %f" % (list_size, end_time-start_time))

# Checks the speed of the second approach (O(n)). Doesn't take that long to execute.
for list_size in range(1000,10001, 1000):
    a_list = [randrange(100000) for x in range(list_size)]
    start_time = time.time()
    print(find_min_value(a_list))
    end_time = time.time()
    print("Size: %d time: %f" % (list_size, end_time-start_time))
