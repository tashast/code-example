# python3

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    if b >= a:
        return gcd(a, b % a)

nums = (input()).split()
n, m = int(nums[0]), int(nums[1])

print(gcd(n, m))