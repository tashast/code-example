# python3

def pisano(n, m):
    a, b = 0, 1
    result = []
    for i in range(n + 1):
        result.append(a)
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            break
    return result


def fib_mod(n, m):
    res = pisano(n, m)
    return res[n % len(res)]

nums = (input()).split()
n, m = int(nums[0]), int(nums[1])

print(fib_mod(n, m))