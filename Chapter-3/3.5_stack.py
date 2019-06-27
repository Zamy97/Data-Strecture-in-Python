# from pythonds.basic.stack import Stack
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



###################### Different implementation of stack #######################

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,tiem)

    def pop(self):
        return self.items.pop(0)

    def peeks(self):
        return self.items[0]

    def size(self):
        return len(self.items)
#################### Testing the Stack Class ####################


example_stack = Stack()
# print(example_stack.isEmpty())
example_stack.push(4)
example_stack.push("Dog")
print(example_stack.peek())
print(example_stack.isEmpty())
example_stack.push(True)
print(exam.size())
print(example_stack.isEmpty())
example_stack.push(8.4)
print(example_stack.pop())
print(example_stack.pop())
print(example_stack.size())
