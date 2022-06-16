def island():
    ssum = sum(arr)
    max_v = max(arr)
    ans = ssum - max_v
    return ans

N = int(input())
arr = list(map(int, input().split()))
print(island())