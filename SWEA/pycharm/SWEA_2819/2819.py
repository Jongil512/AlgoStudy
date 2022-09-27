import sys
sys.stdin = open('2819_input.txt')

def DFS(n, ci, cj, num):
    if n == 7:
        if num not in ans:
            ans.append(num)
        return

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci+di, cj+dj
        if 0 <= ni < 4 and 0 <= nj <4:
            DFS(n+1, ni, nj, num*10+arr[ni][nj])

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans = []
    for i in range(4):
        for j in range(4):
            DFS(0, i, j, 0)
    print(f'#{tc} {len(ans)}')