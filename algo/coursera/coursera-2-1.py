# python3

def fib(n):
    if n < 2:
        return n
    a, b, cur = 0, 1, 2
    while cur <= n:
        a, b, cur = b, a + b, cur + 1
    return b

n = int(input())

print(fib(n))