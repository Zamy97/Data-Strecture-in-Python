import timeit
import random

for i in range(1000, 1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i, "from __main__ import random,x")
    x= list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time=t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
# Done with listing 6 starting 7
