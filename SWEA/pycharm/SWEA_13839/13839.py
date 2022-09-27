import sys
sys.stdin = open('13839_input.txt')

def subset():
    ans = []
    subsets = [[]]
    for num in arr:
        size = len(subsets)
        for i in range(size):
            subsets.append(subsets[i]+[num])
    for i in range(len(subsets)):
        if sum(subsets[i]) == K:
            ans.append(subsets[i])
    return len(ans)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {subset()}')