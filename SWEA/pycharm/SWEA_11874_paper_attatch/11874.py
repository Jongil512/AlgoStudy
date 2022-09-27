import sys
sys.stdin = open('11874_input.txt')

def paper(n):
    if n > 1:
        return paper(n-1) + 2 * paper(n-2)
    else:
        return 1
    # memo = [1, 1]
    # for i in range(2, 31):
    #     memo.append(memo[i-1] + 2 * memo[i-2])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {paper(N//10)}')