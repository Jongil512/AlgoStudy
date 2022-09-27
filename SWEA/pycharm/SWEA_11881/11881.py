import sys
sys.stdin = open('11881_input.txt')

def win(r1, r2):
    if card[r1] == card[r2]:
        return r1
    else:
        if card[r1] == 1 and card[r2] == 2:
            return r2
        elif card[r1] == 1 and card[r2] == 3:
            return r1
        elif card[r1] == 2 and card[r2] == 3:
            return r2
        elif card[r1] == 2 and card[r2] == 1:
            return r1
        elif card[r1] == 3 and card[r2] == 1:
            return r2
        elif card[r1] == 3 and card[r2] == 2:
            return r1


def game(left, right):
    # basis 파트
    if left == right:
        return left

    # 유도 파트
    else:
        r1 = game(left, (left + right)//2)
        r2 = game((left + right)//2 + 1, right)
        return win(r1, r2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = [0] + list(map(int, input().split()))  # [0, 1, 2, 3, 4]
    print(f'#{tc} {game(1, N)}')