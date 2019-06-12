import timeit
x = list(range(2000000))

pop_start= timeit.Timer("x.pop(0)", "from __main__ import x")

pop_end = timeit.Timer("x.pop()", "from __main__ import x")

print("         pop(0)            pop()")
for i in range(1000000, 10000001, 1000000):
    x = list(range(i))
    pt = pop_end.timeit(number = 1000)
    x = list(range(i))
    pz=pop_start.timeit(number = 1000)
    print("%15.5f, %15.5f" %(pz, pt))
