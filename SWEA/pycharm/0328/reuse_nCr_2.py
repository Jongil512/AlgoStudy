# nHr

def comb(k, s):
    if k == R:
        print(*t)
    else:
        for i in range(s, N):
            t[k] = arr[i]
            comb(k + 1, i)

arr = [1, 2, 3]
N = len(arr)
R = 2
t = [0] * R
comb(0, 0)