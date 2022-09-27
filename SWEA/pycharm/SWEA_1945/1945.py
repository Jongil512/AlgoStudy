import sys
sys.stdin = open('1945_input.txt')

def soinsoo(n):
    num_list = [2, 3, 5, 7, 11]
    cnt = [0] * n
    for i in range(5):
        while n % num_list[i] == 0:
            n = n / num_list[i]
            cnt[i] += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}', soinsoo(N))