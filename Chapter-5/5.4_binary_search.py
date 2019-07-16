def binary_search(a_list, item):
    first_item = 0
    last_item = len(a_list) - 1
    found_yet = False

    while first_item <= last_item and not found_yet:
        midpoint = (first_item + last_item) //  2
        if a_list[midpoint] == item:
            found_yet = True
        else:
            if item < a_list[midpoint]:
                last_item = midpoint - 1
            else:
                first_item = midpoint + 1
    return found_yet

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
