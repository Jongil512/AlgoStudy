import sys
sys.stdin = open('1952_input.txt')

def cal_cost(n, cost):
    global ans
    if n > 12:
        if ans > cost:
            ans = cost
        return
    else:
        cal_cost(n + 1, cost + plan[n] * day_c)
        cal_cost(n + 1, cost + mon1)
        cal_cost(n + 3, cost + mon3)
        cal_cost(n + 12, cost + year)
    return ans

T = int(input())
for tc in range(1, T+1):
    day_c, mon1, mon3, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    ans = 123756289
    print(f'#{tc} {cal_cost(1, 0)}')