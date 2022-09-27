import sys
sys.stdin = open('11763_input.txt')

# def perm(n, k):
#     global min_v
#     if k == n:
#         a = position[0]
#         ssum = 0
#         for i in position[1:]:
#             ssum += arr[a][i]
#             a = i
#         if ssum < min_v:
#             min_v = ssum
#         return
#
#     else:
#         for i in range(2, n + 1):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 position[k] = i
#                 perm(n, k + 1)
#                 visited[i] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
#     lst = list(range(1, N+1))
#     min_v = 999999
#     position = [0] * (N+1)
#     visited = [0] * (N+1)
#     position[0] = position[-1] = 1
#     visited[0] = 1
#     perm(N, 1)
#     print(f'#{tc} {min_v}')
#

def perm(n, k):
    if n == k:

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = [0] * N
    perm(N, 0)