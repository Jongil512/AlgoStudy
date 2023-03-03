# 시간초과..
# def solution(n):
#     if n < 3:
#         if n == 0:
#             return 0
#         else:
#             return 1
#     else:
#         return (solution(n-1) + solution(n-2)) % 1234567

def solution(n):
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b % 1234567