def milk():
    q = [0]
    cnt = 0
    for i in range(N):
        if store[i] == q[0]:
            if q[0] == 0:
                q.append(1)
                q.pop(0)
                cnt += 1
            elif q[0] == 1:
                q.append(2)
                q.pop(0)
                cnt += 1
            else:
                q.append(0)
                q.pop(0)
                cnt += 1
    return cnt

N = int(input())
store = list(map(int, input().split()))
print(milk())