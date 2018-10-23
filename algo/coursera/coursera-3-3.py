# python3

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_s = sorted(a)
b_s = sorted(b)

c = [x * y for x, y in zip(a_s, b_s)]
print(sum(c))


