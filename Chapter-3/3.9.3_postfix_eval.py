from pythonds.basic import Stack

def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            result = do_math(token, operand_1, operand_2)
            operand_stack.push(result)
    return operand_stack.pop()

def do_math(operator, operand_1, operand_2):
    if operator == "*":
        return operand_1 * operand_2
    elif operator == "/":
        return operand_1 / operand_2
    elif operator == "+":
        return operand_1 + operand_2
    else:
        return operand_1 - operand_2

print(postfix_eval('7 8 + 3 2 + /'))
