def points(intervals):
    s = sorted(intervals, key=lambda x: x[1])
    res = []
    pt = s[0][1]
    res.append(pt)
    for el in s:
        if el[0] <= pt <= el[1]:
            continue
        else:
            pt = el[1]
            res.append(pt)
    return res


def main():
    n = int(input())
    intervals = []
    for i in range(n):
        nums = input().split()
        intervals.append((int(nums[0]), int(nums[1])))

    pts = points(intervals)

    print(len(pts))
    print(*pts, sep=' ')


if __name__ == "__main__":
    main()