import sys
sys.stdin = open('14034_input.txt')

def shelf(n, ssum):
    global ans
    if ssum >= B + ans:
        return

    if n == N:
        if ssum >= B and ans > ssum - B:
            ans = ssum - B
        return

    shelf(n+1, ssum + arr[n])        # 포함하는 경우
    shelf(n+1, ssum)                 # 포함하지 않는 경우

    return ans

    # ans = []
    # subsets = [[]]
    # for num in arr:
    #     size = len(subsets)
    #     for i in range(size):
    #         subsets.append(subsets[i] + [num])
    # for i in range(len(subsets)):
    #     if sum(subsets[i]) >= B:
    #         ans.append(sum(subsets[i]))
    # return min(ans) - B

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 12345786
    print(f'#{tc} {shelf(0, 0)}')