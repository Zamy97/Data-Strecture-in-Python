from pythonds.basic import Deque

def pal_checker(a_string):
    character_deque = Deque()
    for character in a_string:
        character_deque.addRear(character)

    still_equal = True

    while character_deque.size() > 1 and still_equal:
        first = character_deque.removeFront()
        last = character_deque.removeRear()
        if first != last:
            still_equal = False

    return still_equal

print(pal_checker("aktar"))
print(pal_checker("radar"))
print(pal_checker("Rahima"))
print(pal_checker("toot"))
