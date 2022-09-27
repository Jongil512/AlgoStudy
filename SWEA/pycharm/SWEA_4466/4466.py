import sys
sys.stdin = open('4466_input.txt')

def score():
    ans_list = sorted(arr)
    total = 0
    for i in range(1, K+1):
        total += ans_list[-i]

    return total

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {score()}')