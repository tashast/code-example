# python3

line = input().split()
n, W = int(line[0]), int(line[1])
items = []

for i in range(n):
    line = input().split()
    c, w = int(line[0]), int(line[1])
    items.append((c, w))


free_w = W
sum_c = 0

items_s = sorted(items, key=lambda x: x[0]/x[1], reverse=True)

i = 0
while free_w > 0 and i < n:
    c, w = items_s[i][0], items_s[i][1]
    if w <= free_w:
        sum_c += c
        free_w -= w
    else:
        sum_c += c * free_w / w
        free_w = 0
    i += 1

print(sum_c)
