# python3

n = int(input())

low = 1
upp = n
res = []

while low < upp/2:
    res.append(low)
    upp -= low
    low += 1

res.append(upp)

print(len(res))
print(*res, sep = ' ')