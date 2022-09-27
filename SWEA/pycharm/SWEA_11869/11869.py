import sys
sys.stdin = open('11869_input.txt')

def compare_str(a, b):
    for i in range(len(b)-len(a)+1):
        if b[i:i+len(a)] == a:
            return 1
    return 0

    # def brute_force(p, t):
    #     M = len(p)
    #     N = len(t)
    #     for i in range(N - M + 1):
    #         flag = 1
    #         for j in range(M):
    #             if t[i + j] != p[j]:
    #                 flag = 0
    #                 break
    #         if flag:
    #             return 1
    #     return 0

    # T = int(input())
    # for tc in range(1, T + 1):
    #     p = input()
    #     t = input()
    #
    #     print(f'#{tc} {brute_force(p, t)}')

T = int(input())
for tc in range(1, T + 1):
    A = list(input())
    B = list(input())
    print(f'#{tc} {compare_str(A, B)}')