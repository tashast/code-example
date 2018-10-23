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


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()