
def parenthesis_checker(symbol_strings):
    symbol_stack = Stack()
    balanced = True
    index = 0
    while index < len(symbol_strings) and balanced:
        symbol = symbol_strings[index]
        if symbol == "(":
            symbol_stack.push(symbol)
        else:
            if symbol_stack.isEmpty():
                balanced = False
            else:
                symbol_stack.pop()

    if balanced and symbol_stack.isEmpty():
        return True
    else:
        return False

print(parenthesis_checker('((()))'))
print(parenthesis_checker('(()'))
