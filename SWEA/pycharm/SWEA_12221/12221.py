import sys
sys.stdin = open('12221_input.txt')

def sh():
    if 1 <= N <= 9 and 1 <= M <= 9:
        return N * M
    return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {sh()}')