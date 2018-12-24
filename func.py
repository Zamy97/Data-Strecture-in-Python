# import random
# def square(n):
#     return n**2
#
# print(square(square(3)))

# Infinite monkey theorem
def generate_one(strlen):
    alphabet = "abcdefghijklmnopqurstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]

    return res

def score(goal, teststring):
    num_same = 0
    for i in range(len(goal)):
        if goal[1] == teststring[1]:
            num_same = num_same + 1
    return num_same/len(goal)

def main():
    goalstring = "methinks it is like wesele"
    new_string = generate_one(28)
    best = 0
    new_score = score(goalstring, new_string)

    while new_score < 1:
        if new_score >= best:
            print(new_string)
            best = new_score
        new_string = generate_one(28)
        new_score = score(goalstring, new_string)
