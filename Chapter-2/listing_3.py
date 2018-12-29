import timeit
# Creates a list of numbers by concatenation
def test1():
    list_1 = []
    for i in range(1000):
        list_1 = list_1 + [i]
    return list_1


# Creates a list of number from a range using the append method
def test2():
    list_2 = []
    for i in range(1000):
        list_2.append(i)
    return list_2


# Creating a list of numbers from a range using list comprehension
def test3():
    list_3 = [i for i in range(1000)]
    return list_3


# Making a list of numbers using the range function wrapped by a call to the list constructor
def test4():
    list_4 = list(range(1000))
    return list_4

#Testing the time for each of these function to run to create the list using timeit method
t1 = timeit.Timer("test1()", "from __main__ import test1")
print("Cancatinating takes ", t1.timeit(number=1000), "miliseconds") # Takes about 1.333 miliseconds

t2 = timeit.Timer("test2()", "from __main__ import test2")
print("Appending takes ", t2.timeit(number=1000), "miliseconds")

t3 = timeit.Timer("test3()", "from __main__ import test3")
print("Comprehension takes ", t3.timeit(number=1000), "miliseconds")

t4 = timeit.Timer("test4()", "from __main__ import test4")
print("List range takes ", t4.timeit(number=1000), "miliseconds")
