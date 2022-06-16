import sys
sys.stdin = open('10580_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [0] * 10001
    for i in range(N):
        s, e = map(int, input().split())
        for j in range(s, e+1):
            visited[j] += 1
    cnt = 0
    for k in range(1, 10001):
        if visited[k] > 1:
            cnt += 1
    print(f'#{tc} {cnt}')