class Stack():
    def __init__(self):
        self.items = []

    # Checks to see if the stack is empty or not. Returns a boolean value
    def isEmpty(self):
        return self.items == []

    # Adds a new item to the tp of the stack. Return nothing.
    def push(self):
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
