import sys
n = int(input())

max_stack = [0]

for line in sys.stdin:
    line = line.rstrip()
    if line == 'max':
        print(max_stack[-1])
    elif line == 'pop':
        max_stack.pop()
    else:
        number = int(line.split()[1])
        max_stack.append(max(number, max_stack[-1]))