import sys
sys.stdin = open('1210_input.txt')

# dx, dy로 좌, 우, 상 인덱스를 구성해놓고 찾아가며 탐색

def ladder(arr):
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    for j in range(100):
        if arr[99][j] == 2:
            a = 99
            b = j
            break
    while a > 0:
        for i in range(3):
            if 0 <= b + dy[i] <= 99:
                if arr[a + dx[i]][b + dy[i]] == 1:
                    arr[a][b] += 1
                    a, b = a + dx[i], b + dy[i]
                    break
    return b

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{tc} {ladder(arr)}')