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
    """
    Checks the letters in lists to see if it exists in both lists and returns true.

    """

    # Converts the given string into a list
    a_list1 = list(string1)
    a_list2 = list(string2)

    # sort the list alphabatically
    a_list1.sort()
    a_list2.sort()

    position = 0
    matches = True

    while position < len(string1) and matches:
        if a_list1[position] == a_list2[position]:
            position = position + 1
        else:
            matches = False

    return matches

print(anagram_solution2('abcdejhfre','edcbajh'))


# Third solution using count and compare

def anagramSolution4(string1,string2):
    count1 = [0]*26
    count2 = [0]*26

    for i in range(len(string1)):
        position = ord(string1[i])-ord('a')
        count1[position] = count1[position] + 1

    for i in range(len(string2)):
        position = ord(string2[i])-ord('a')
        count2[position] = count2[position] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if count1[j]==count2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagramSolution4('apple','pleap'))
# a_word = "aktar"
# a_word_to_list = list(a_word)
# a_word_to_list.sort()
# print(a_word_to_list)
