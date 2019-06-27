class Stack():
    def __init__(self):
        self.items = []

    # Checks to see if the stack is empty or not. Returns a boolean value
    def isEmpty(self):
        return self.items == []

    # Adds a new item to the tp of the stack. Return nothing.
    def push(self, item):
        self.items.append(item)

    # Removes and return the top item from the stack
    def pop(self):
        return self.items.pop()

    #Retuns the top item from the stack but doesn't modify it.
    def peek(self):
        return self.items[len(self.items)-1]

    #Retuns the size of the Stack
    def size(self):
        return len(self.items)



#### Divide by two algoriths to convert a decimial number to a binary number
def divide_by_2(desimal_num):
    reminder_stack = Stack()

    while desimal_num > 0:
        remainder = desimal_num % 2
        reminder_stack.push(remainder)
        desimal_num = desimal_num // 2

    binary_string = ''
    while not reminder_stack.isEmpty():
        binary_string = binary_string + str(reminder_stack.pop())
    return binary_string
print(divide_by_2(42))
