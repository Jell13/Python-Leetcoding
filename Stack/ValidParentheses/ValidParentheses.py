def valid(s):
    stack = []
    checker = {')':'(', ']':'[', '}':'{'}

    for c in s:
        if c not in checker:
            stack.append(c)
        else:
            if len(stack) > 0:
                curr_parent = stack.pop()
                if curr_parent != checker[c]:
                    return False
            else :
                return False
    return len(stack) == 0