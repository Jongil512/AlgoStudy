import sys
sys.stdin = open('3975_input.txt')

def winner():
    if (A/B) < (C/D):                               # 배열에 우승자를 쭉 넣음
        ans.append('BOB')
    elif (A/B) > (C/D):
        ans.append('ALICE')
    else:
        ans.append('DRAW')

ans = []                                            # 배열 생성
T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    win = [0, 0, 0]
    winner()
for i in range(T):                                  # 마지막에 for문으로 출력
    print(f'#{i+1} {ans[i]}')

