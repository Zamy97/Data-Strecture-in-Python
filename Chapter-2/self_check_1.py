## Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. O(n2). The second function should be linear O(n)

def find_min_value(a_list):
    # overall_min = a_list[0]
    for i in a_list:
        is_smallest = True
        for j in a_list:
            if i > j:
                is_smallest = False
        if is_smallest:
            overall_min = i
    return overall_min

print(find_min_value([2,5,1,7,9,9,5,2,1,9,0,3,3,-9]))
