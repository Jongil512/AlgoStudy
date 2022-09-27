import sys
sys.stdin = open('1946_input.txt')

def zip_out(char, n):
    new_list = []
    for i in range(n):
        alpha = char[i][0]
        num = int(char[i][1])
        for j in range(num):
            new_list.append(alpha)
    ans = ''
    cnt = 0
    for i in new_list:
        ans += i
        cnt += 1
        if cnt == 10:
            ans += '\n'
            cnt = 0
    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    char = [list(map(str, input().split())) for _ in range(N)]
    print(f'#{tc}')
    print(zip_out(char, N))