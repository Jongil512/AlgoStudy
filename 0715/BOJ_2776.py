# 암기왕

import sys

def BS(i, s, e):
    while s <= e:
        mid = (s + e) // 2
        if note1[mid] == i:
            return 1
        elif note1[mid] <= i:
            s = mid + 1
        else:
            e = mid - 1
    return 0


T = int(sys.stdin.readline().rstrip())
for tc in range(T):
    N = int(sys.stdin.readline().rstrip())
    note1 = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    note2 = list(map(int, sys.stdin.readline().rstrip().split()))

    note1.sort()
    s = 0
    e = N-1

    for i in range(M):
        print(BS(note2[i], s, e))