# python3

def coins(m):
    c_10 = m // 10
    m = m % 10
    c_5 = m // 5
    m = m % 5
    return c_10 + c_5 + m

m = int(input())
print(coins(m))