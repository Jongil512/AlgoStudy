def laundry(n):
    exchange = [25, 10, 5, 1]
    for i in range(len(exchange)):
        cnt[i] = n // exchange[i]
        n -= exchange[i] * cnt[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 4
    laundry(N)
    print(*cnt)