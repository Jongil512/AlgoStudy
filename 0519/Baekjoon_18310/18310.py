# 안테나

def func():
    # 중간값 중 중복되는 경우 분할
    houses.sort()
    if N % 2:
        ans = houses[N//2]
    else:
        i = N//2 - 1
        ans = houses[i]
    return ans

N = int(input())
houses = list(map(int, input().split()))
print(func())