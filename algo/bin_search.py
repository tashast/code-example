def bs(arr, low, high, key):
    if high < low:
        return -1
    mid = (high + low)//2
    if key == arr[mid]:
        return mid+1
    elif key < arr[mid]:
        return bs(arr, low, mid-1, key)
    elif key > arr[mid]:
        return bs(arr, mid+1, high, key)
    return -1


line1 = input().split()
n = int(line1[0])
arr = [int(x) for x in line1[1:]]
line2 = input().split()
k = int(line2[0])
ks = [int(x) for x in line2[1:]]

ans = []
for key in ks:
    ans.append(bs(arr, 0, (n-1), key))
print(*ans, sep=' ')