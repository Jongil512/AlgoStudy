def alpha_abst():
    global ans
    for j in range(k):
        max_idx = 0
        max_value = min(alphabet)
        for i in range(N):
            if not used[i]:
                if alphabet[i] > max_value:
                    max_value = alphabet[i]
                    max_idx = i
        used[max_idx] = alphabet[max_idx]

    for i in range(N):
        if used[i]:
            ans += used[i]
    return ans

alphabet = 'zfhkxnvnlynev'
k = 3
N = len(alphabet)
used = [''] * N
ans = ''
print(alpha_abst())