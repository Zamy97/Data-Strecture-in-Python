# First Solution (Checking off)

def anagram_solution1(string1, string2):
    """
    This function checls every position in string2 to see if the chacarecter from string1 exist in string 2.

    """
    a_list = list(string2)

    position1 = 0
    still_ok = True

    while position1 < len(string1) and still_ok:
        position2 = 0
        found = False
        while position2 < len(a_list) and not found:
            if string1[position1] == a_list[position2]:
                found = True
            else:
                position2 = position2 + 1

        if found:
            a_list[position2] = None
        else:
            still_ok = False

        position1 = position1 + 1

    return still_ok

print(anagram_solution1('world', 'dwlro'))

# Second Solution by soring and comparing

def anagram_solution2(string1, string2):
    a_list1 = list(string1)
    a_list2 = list(string2)
