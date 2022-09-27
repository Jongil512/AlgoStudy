# def snail_nums(arr, st, le, num):
#     last = st + le - 1
#     for c in range(st, le):
#         arr[st][c] = num
#         num += 1
#     for r in range(st + 1, last + 1):
#         arr[r][last] = num
#         num += 1
#     for c in range(last - 1, st - 1, -1):
#         arr[last][c] = num
#         num += 1
#     for r in range(last - 1, st, -1):
#         arr[r][st] = num
#         num += 1
#     return arr
#
#
#
# N = 5
# snail = [[0 for j in range(N)] for i in range(N)]
# ans = snail_nums(snail, 0, N, 1)
# print(ans)

arr = [1, 2, 3, 4, 5]
for i in range(5):
    print(arr[-(i//2)-1])
    print(arr[-5])