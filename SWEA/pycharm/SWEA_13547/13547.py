import sys
sys.stdin = open('13547_input.txt')

def cal():
    cnt = 0
    for i in range(len(res)):
        # 'o'가 나오면 카운트 증가
        if res[i] == 'o':
            cnt += 1
    # 남은 횟수와 현재 카운트 비교
    if 15 - len(res) >= 8 - cnt:
        return 'YES'
    else:
        return 'NO'

T = int(input())
for tc in range(1, T+1):
    res = list(input())
    print(f'#{tc} {cal()}')