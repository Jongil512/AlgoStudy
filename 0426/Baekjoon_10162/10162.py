N = int(input())
cnt = [0, 0, 0]
button = [300, 60, 10]

for i in range (len(button)):
    if N // button[i] >= 1:
        cnt[i] += N // button[i]
        N -= button[i] * (N // button[i])
        if N == 0:
            break
if N > 0:
    print(-1)
else:
    print(*cnt)