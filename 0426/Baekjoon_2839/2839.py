N = int(input())
max_cnt = -1
cnt_3 = 0
M = N // 5
for i in range(0, M+1):
    if (N - (i*5)) % 3 == 0:
        if i > max_cnt:
            max_cnt = i
            cnt_3 = (N - (i*5)) // 3
if max_cnt == -1 and cnt_3 == 0:
    print(max_cnt)
else:
    print(max_cnt + cnt_3)