# a = 5
# b = 6
# c = 10
# for i in range(n):
#     for j in range(n):
#         x = i * i
#         y = j * j
#         z = i * j
# for k in range(n):
#     w = a*k + 45
#     v = b*b
# d = 33

## self check
import time
from random import randrange

#n^2 solution

def min_number(some_list):
    # overall_min = some_list[0]
    for a_number in some_list:
        is_smallest = True
        for j in some_list:
            if a_number > j:
                is_smallest = False
        if is_smallest:
            overall_min = a_number
    return overall_min
print(min_number([5,4,-9,2,7]))
print(min_number([-9,5,1,4,9]))

# Linear Solution
