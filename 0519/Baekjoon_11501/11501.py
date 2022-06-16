# 주식

def func(days):
    ans = 0
    while days:
        M = days.index(max(days))
        for i in range(M):
            ans += days[M] - days[i]
        if M == len(days)-1:
            break
        else:
            days = days[M+1:]
    ans_lst.append(ans)

ans_lst = []
T = int(input())
for tc in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    func(days)
for i in range(len(ans_lst)):
    print(ans_lst[i])