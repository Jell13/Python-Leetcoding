def evalRPN(tokens):
    stack = []
    operands = {"+", "-", "*", "/"}
    for c in tokens:
        if c not in operands:
            stack.append(int(c))
        else:
            if c == "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif c == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif c == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif c == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))

    return stack.pop()