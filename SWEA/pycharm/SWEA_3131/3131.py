import math

def sosu():
    ans = []
    for i in range(2, 1000001):
        flag = 1
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                flag = 0
                break
        if flag:
            ans.append(i)

    return ans

print(*sosu())