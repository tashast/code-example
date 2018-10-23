# python 3

n = int(input())
digits = list(map(int, input().split()))

dig = sorted(digits, reverse = True)
print(*dig)