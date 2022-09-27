N = int(input())
Q = []
for i in range(1, N+1):
    Q.append(i)
while len(Q) > 1:
    Q.pop(0)
    r = Q.pop(0)
    Q.append(r)
print(*Q)