from collections import deque

BINARY = ['+', '-', '/', '^']
TERNARY = '~'

def poliz(string):
    expr = string.split()
    res = deque([])
    for elem in expr:
        if elem == TERNARY:
            if len(res) == 1:
                return -res.pop()
            else:
                raise AssertionError
        elif elem in BINARY:
            if len(res) < 2:
                raise AssertionError
            else:
                num2 = res.pop()
                num1 = res.pop()
                if elem == '+':
                    num_res = num1 + num2
                    res.append(num_res)
                elif elem == '-':
                    num_res = num1 - num2
                    res.append(num_res)
                elif elem == '/':
                    if num2 == 0:
                        raise AssertionError
                    else:
                        num_res = num1 / num2
                        res.append(num_res)
                elif elem == '^':
                    if num1 == 0 and num2 < 0:
                        raise AssertionError
                    elif num2 > 3000000000:
                        raise AssertionError
                    else:
                        num_res = num1 ** num2
                        res.append(num_res)
        else:
            res.append(int(elem))
    return res.pop()
