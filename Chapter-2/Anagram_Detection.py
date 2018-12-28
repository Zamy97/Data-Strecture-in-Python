def anagram_solution(string1, string2):
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

print(anagram_solution('Aktar', 'dcba'))
