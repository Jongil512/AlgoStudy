N = int(input())

def jinsu_2(N):
    if N // 2 == 0:
        return str(N % 2)
    return jinsu_2(N // 2) + str(N % 2)

print(jinsu_2(N))
