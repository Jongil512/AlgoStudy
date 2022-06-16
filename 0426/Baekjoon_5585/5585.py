N = int(input())

M = 1000 - N
cnt = 0
exchange = [500, 100, 50, 10, 5, 1]

for i in range (len(exchange)):
    if M // exchange[i] >= 1:
        cnt += M // exchange[i]
        M -= exchange[i] * (M // exchange[i])
        if M == 0:
            break
print(cnt)