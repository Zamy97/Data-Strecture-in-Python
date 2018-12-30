import timeit
x = list(range(2000000))

pop_start= timeit.Timer("x.pop(0)", "from __main__ import x")
print("The first pop method takes ", pop_start.timeit(number=1000), "miliseconds.") # Takes about 2.103 miliseconds


pop_end = timeit.Timer("x.pop()", "from __main__ import x")
print("The Second pop method takes ", pop_end.timeit(number = 1000), "miliseconds")
