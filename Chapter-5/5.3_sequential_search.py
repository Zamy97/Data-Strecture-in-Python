def sequential_search(a_list, item):
    position = 0
    found = False

    while position < len(a_list) and not found:
        if a_list[position] == item:
            found = True
        else:
            position = position + 1

    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(testlist, 3))
print(sequential_search(testlist, 13))


def ordered_sequential_search(a_list, item):
    position = 0
    found = False
    stop = False

    while position < len(a_list) and not found and not stop:
        if a_list[position] == item:
            found = True
        else:
            if a_list[position] > item:
                stop = True
            else:
                position = position + 1
    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(ordered_sequential_search(testlist, 3))
print(ordered_sequential_search(testlist, 13))
