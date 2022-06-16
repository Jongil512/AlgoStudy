import sys
sys.stdin = open('3408_input.txt')

# def triple_sum(S1, S2, S3, N):
    # number = [0] + list(range(1, N*2+1))
    # S1 = sum(number[:N + 1])
    #
    # for i in range(len(number)):
    #     if number[i] % 2:
    #         S2 += i
    #     else:
    #         S3 += i
    # return [S1, S2, S3]

def triple_sum(n):
    S1 = n * (n + 1) // 2
    S2 = n ** 2
    S3 = n ** 2 + n
    return S1, S2, S3

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}', *triple_sum(N))