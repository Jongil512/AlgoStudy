import sys
sys.stdin = open('1240_input.txt')

code = [[[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]

code[0][0][0][1][1][0][1] = 0
code[0][0][1][1][0][0][1] = 1
code[0][0][1][0][0][1][1] = 2
code[0][1][1][1][1][0][1] = 3
code[0][1][0][0][0][1][1] = 4
code[0][1][1][0][0][0][1] = 5
code[0][1][0][1][1][1][1] = 6
code[0][1][1][1][0][1][1] = 7
code[0][1][1][0][1][1][1] = 8
code[0][0][0][1][0][1][1] = 9

def find_pos(arr):      # 뒤에서 1찾기
    for i in range(r):
        for j in range(c-1, -1, -1):
            if arr[i][j] == 1:
                return i, j

T = int(input())
for tc in range(1, T+1):
    r, c = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(r)]
    sx, sy = find_pos(arr)

    for i in range(8):
        sy -= 7
    sy += 1

    a_code = []         # 암호 코드
    a_value = 0         # 암호 검증
    for i in range(8):
        a_code.append(code[arr[sx][sy]][arr[sx][sy+1]][arr[sx][sy+2]][arr[sx][sy+3]][arr[sx][sy+4]][arr[sx][sy+5]][arr[sx][sy+6]])
        sy += 7
    a_value = (a_code[0] + a_code[2] + a_code[4] + a_code[6]) * 3 + a_code[1] + a_code[3] + a_code[5] + a_code[7]

    if a_value % 10 == 0:
        print(f'#{tc} {sum(a_code)}')
    else:
        print(f'#{tc} 0')