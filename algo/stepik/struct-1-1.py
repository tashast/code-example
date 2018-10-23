BRACKETS_DICT = {')': '(', '}': '{', ']': '['}

def neat_check(brackets):
    stack_br = []
    for idx, bracket in enumerate(brackets, start=1):
        if bracket in BRACKETS_DICT.values():   # opening
            stack_br.append((bracket, idx))
        elif bracket in BRACKETS_DICT:
            if len(stack_br) == 0:
                print("exit by len 0")
                return idx
            top_bracket, ind = stack_br.pop()
            if BRACKETS_DICT[bracket] != top_bracket:
                print('exit by non-match')
                return idx
    print('exit in the end')
    return stack_br.pop()[1] if stack_br else 'Success'
