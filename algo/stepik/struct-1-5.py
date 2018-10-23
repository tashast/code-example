n = int(input())
arr = [int(x) for x in input().split()]
m = int(input())

stack_push = arr[:m]
stack_pop = []
pop_max = [0]
push_max = max(stack_push)
max_list = []


def transfer():
    global push_max
    push_max = 0
    while stack_push:
        top = stack_push.pop()
        stack_pop.append(top)
        pop_max.append(max(top, pop_max[-1]))


transfer()
idx = m

while idx < len(arr):
    max_list.append(max(push_max, pop_max[-1]))
    if not stack_pop:
        transfer()
    stack_pop.pop()
    pop_max.pop()
    new_el = arr[idx]
    stack_push.append(new_el)
    push_max = max(push_max, new_el)
    idx += 1

max_list.append(max(push_max, pop_max[-1]))
print(*max_list, sep = ' ')