import sys
sys.stdin = open('1970_input.txt')

def exchange(n):
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * len(money_list)
    for i in range(len(money_list)):
        cnt[i] = n // money_list[i]
        n -= cnt[i] * money_list[i]
    return cnt

T = int(input())
for tc in range(1, T + 1):
    money = int(input())
    print(f'#{tc}')
    print(*exchange(money))
