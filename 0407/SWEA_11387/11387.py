import sys
sys.stdin = open('11387_input.txt')

# 몬스터 사냥

def slayer():
    total = 0
    # N번의 공격 후의 데미지
    for i in range(N):
        # 매 공격마다 누적
        total += D * (1 + i * L * 0.01)
    return int(total)

T = int(input())
for tc in range(1, T+1):
    D, L, N = map(int, input().split())
    print(f'#{tc} {slayer()}')