import sys
sys.stdin = open('3499_input.txt')

def perfect_shuffle():
    ans = []
    if N % 2:
        for i in range(N//2):
            ans.append(arr[i])
            ans.append(arr[N // 2 + i + 1])
        ans.append(arr[N//2])
    else:
        for i in range(N//2):
            ans.append(arr[i])
            ans.append(arr[N // 2 + i])
    return ' '.join(ans)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    print(f'#{tc}', perfect_shuffle())