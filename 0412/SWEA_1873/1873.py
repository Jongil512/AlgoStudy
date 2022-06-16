import sys
sys.stdin = open('1873_input.txt')

# 배틀필드

def battlefield(tankX, tankY):
    for i in range(len(command)):
        if command[i] == 'U':
            arr[tankX][tankY] = '^'
            if 0 <= tankX + dx[0] < H and 0 <= tankY + dy[0] < W:
                if arr[tankX + dx[0]][tankY + dy[0]] == '.':
                    arr[tankX][tankY] = '.'
                    tankX = tankX + dx[0]
                    tankY = tankY + dy[0]
                    arr[tankX][tankY] = '^'

        elif command[i] == 'D':
            arr[tankX][tankY] = 'v'
            if 0 <= tankX + dx[1] < H and 0 <= tankY + dy[1] < W:
                if arr[tankX + dx[1]][tankY + dy[1]] == '.':
                    arr[tankX][tankY] = '.'
                    tankX = tankX + dx[1]
                    tankY = tankY + dy[1]
                    arr[tankX][tankY] = 'v'

        elif command[i] == 'L':
            arr[tankX][tankY] = '<'
            if 0 <= tankX + dx[2] < H and 0 <= tankY + dy[2] < W:
                if arr[tankX + dx[2]][tankY + dy[2]] == '.':
                    arr[tankX][tankY] = '.'
                    tankX = tankX + dx[2]
                    tankY = tankY + dy[2]
                    arr[tankX][tankY] = '<'

        elif command[i] == 'R':
            arr[tankX][tankY] = '>'
            if 0 <= tankX + dx[3] < H and 0 <= tankY + dy[3] < W:
                if arr[tankX + dx[3]][tankY + dy[3]] == '.':
                    arr[tankX][tankY] = '.'
                    tankX = tankX + dx[3]
                    tankY = tankY + dy[3]
                    arr[tankX][tankY] = '>'

        elif command[i] == 'S':
            if arr[tankX][tankY] == '^':
                bulletX, bulletY = tankX, tankY
                while True:
                    if 0 <= bulletX + dx[0] < H and 0 <= bulletY + dy[0] < W:
                        bulletX = bulletX + dx[0]
                        bulletY = bulletY + dy[0]
                        if arr[bulletX][bulletY] == '*':
                            arr[bulletX][bulletY] = '.'
                            break
                        elif arr[bulletX][bulletY] == '#':
                            break
                    else:
                        break
            elif arr[tankX][tankY] == 'v':
                bulletX, bulletY = tankX, tankY
                while True:
                    if 0 <= bulletX + dx[1] < H and 0 <= bulletY + dy[1] < W:
                        bulletX = bulletX + dx[1]
                        bulletY = bulletY + dy[1]
                        if arr[bulletX][bulletY] == '*':
                            arr[bulletX][bulletY] = '.'
                            break
                        elif arr[bulletX][bulletY] == '#':
                            break
                    else:
                        break
            elif arr[tankX][tankY] == '<':
                bulletX, bulletY = tankX, tankY
                while True:
                    if 0 <= bulletX + dx[2] < H and 0 <= bulletY + dy[2] < W:
                        bulletX = bulletX + dx[2]
                        bulletY = bulletY + dy[2]
                        if arr[bulletX][bulletY] == '*':
                            arr[bulletX][bulletY] = '.'
                            break
                        elif arr[bulletX][bulletY] == '#':
                            break
                    else:
                        break
            elif arr[tankX][tankY] == '>':
                bulletX, bulletY = tankX, tankY
                while True:
                    if 0 <= bulletX + dx[3] < H and 0 <= bulletY + dy[3] < W:
                        bulletX = bulletX + dx[3]
                        bulletY = bulletY + dy[3]
                        if arr[bulletX][bulletY] == '*':
                            arr[bulletX][bulletY] = '.'
                            break
                        elif arr[bulletX][bulletY] == '#':
                            break
                    else:
                        break
    return arr

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input(). split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    command = list(input())
    tankX, tankY = 0, 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] in ['^', 'v', '>', '<']:
                tankX, tankY = i, j
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    battlefield(tankX, tankY)
    print(f'#{tc}', end=' ')
    for i in range(H):
        print(''.join(arr[i]))