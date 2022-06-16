def reverse_S():
    N = len(S)
    cnt_0 = cnt_1 = 0
    for i in range(N-1):
        if S[i] == '0':
            if S[i+1] == '0':
                continue
            else:
                cnt_0 += 1
        else:
            if S[i+1] == '1':
                continue
            else:
                cnt_1 += 1
    return max(cnt_0, cnt_1)

S = input()
print(reverse_S())