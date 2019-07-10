from pythonds.basic import Queue

def hot_potato_simulator(name_list, num):
    simple_queue = Queue()
    for name in name_list:
        simple_queue.enqueue(name)

    while simple_queue.size() > 1:
        for i in range(num):
            simple_queue.enqueue(simple_queue.dequeue())

        simple_queue.dequeue()

    return simple_queue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
