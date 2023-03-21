import math

def solution(arr):
    while len(arr) >= 2:
        a = arr.pop()
        b = arr.pop()
        arr.append((a*b)//int(math.gcd(a, b)))
    return arr[0]

# print(solution([2,6,8,14]))
# print(solution([1,2,5]))
print(solution([2,6,11,17]))
# print(solution([2,6,7,24]))