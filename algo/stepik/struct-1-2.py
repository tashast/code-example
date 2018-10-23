n = int(input())
parents = [int(x) for x in input().split()]
heights = {}

for v in range(n):
    height = 1
    p = parents[v]
    while p != -1:
        if p in heights:
            height += heights[p]
            p = -1
        else:
            height += 1
            p = parents[p]
    heights[v] = height

print(max(heights.values()))