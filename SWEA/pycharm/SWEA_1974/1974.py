import sys
sys.stdin = open('1974_input.txt')

def check_sudoku(arr):
    # 숫자 카운팅
    for i in range(9):
        # 숫자 중복 체크를 위한 0 리스트 생성
        cnt = [0] * 10
        # 행 중복 체크 후 중복이면 0 리턴
        for j in range(9):
            cnt[arr[i][j]] += 1
            if cnt[arr[i][j]] >= 2:
                return 0

        # 0 리스트 초기화 후 열 중복 체크
        # 중복이면 0 리턴
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[j][i]] += 1
            if cnt[arr[j][i]] >= 2:
                return 0
    # 3*3 시작점마다
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # 0 리스트 초기화 후
            cnt = [0] * 10
            # 시작점으로부터 행 열 3만큼씩 이동하며 카운팅 후
            # 중복이면 0 리턴
            for k in range(3):
                for l in range(3):
                    cnt[arr[i+k][j+l]] += 1
                    if cnt[arr[j][i]] >= 2:
                        return 0
    # 모두 중복이 아니면 1 리턴
    return 1

T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {check_sudoku(sudoku)}')
