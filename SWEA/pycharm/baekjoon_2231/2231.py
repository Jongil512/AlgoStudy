def boonhae():
    min_v = 99999999
    for i in range(1, N):
        total = 0
        k = i
        while k > 0:
            a = k % 10
            total += a
            k = k // 10
        if total + i == N:
            min_v = i
            return min_v
    return 0

N = int(input())
word_N = str(N)
L = len(word_N)
print(boonhae())