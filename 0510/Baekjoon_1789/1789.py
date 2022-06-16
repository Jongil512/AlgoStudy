# 수들의 합

def sums():
    # 수가 1이라면 1 리턴
    if S == 1:
        return 1
    else:
        sum_lst = []
        ssum = 0
        cnt = 0
        # 차례대로 더하는 게 가장 많이 더할 수 있음
        for i in range(1, S):
            if ssum + i <= S:
                ssum += i
                cnt += 1
                sum_lst.append(i)
            else:
                break
    return cnt

S = int(input())
print(sums())
