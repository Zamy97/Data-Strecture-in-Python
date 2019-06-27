##### Specific parenthesis checker to see if it's balanced or not. Such as each opening parenthesis has to have a closing parenthesis.
def parenthesis_checker(symbol_string):
    symbol_stack = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            symbol_stack.push(symbol)
        else:
            if symbol_stack.isEmpty():
                balanced = False
            else:
                symbol_stack.pop()
        index = index + 1

    if balanced and symbol_stack.isEmpty():
        return True
    else:
        return False

print(parenthesis_checker('((()))'))
print(parenthesis_checker('(()'))
