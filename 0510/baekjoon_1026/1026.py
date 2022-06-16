# 보물

def tresure():
    samplea = sorted(arrA)
    sampleb = sorted(arrB)
    sampleb.reverse()
    S = 0
    for i in range(N):
        S += samplea[i] * sampleb[i]
    return S

N = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
print(tresure())