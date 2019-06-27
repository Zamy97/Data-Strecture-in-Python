#Balanced Symbols (A General Case)
def parenthesis_checker(symbol_string):
    symbol_stack = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '([{':
            symbol_stack.push(symbol)
        else:
            if symbol_stack.isEmpty():
                balanced = False
            else:
                top = symbol_stack.pop()
                if not matches(top,symbol):
                    balanced = False
        index = index + 1
    if balanced and isEmpty:
        return True
    else:
        return False


def matches(open,close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)


print(parenthesis_checker('{{([][])}()}'))
print(parenthesis_checker('[{()]'))
