import sys
from collections import deque

def shuffle(x, cards):
    result = []

    if x < N//2:
        L = deque(cards[:N//2])
        R = deque(cards[N//2:])

        num = N//2 - x
    else:
        L = deque(cards[N//2:])
        R = deque(cards[:N//2])

        num = x - (N//2) + 1

    for _ in range(num):
        result.append(L.popleft())

    while len(R) > num:
        result.append(R.popleft())
        result.append(L.popleft())

    while R:
        result.append(R.popleft())

    return result


def mixed(cnt, cards):
    global ans

    if cnt > ans or cnt > 5:
        return

    if cards == sort_cards or cards == sort_cards_rev:
        ans = min(ans, cnt)
        return

    for i in range(1, N):
        mixed(cnt+1, shuffle(i, cards))


T = int(sys.stdin.readline().rstrip())
for tc in range(1, T+1):
    N = int(sys.stdin.readline().rstrip())
    cards = list(map(int, sys.stdin.readline().rstrip().split()))

    sort_cards = sorted(cards)
    sort_cards_rev = sorted(cards, reverse = True)

    ans = float('inf')

    mixed(0, cards)

    if ans > 5:
        ans = -1

    print(f'#{tc} {ans}')


