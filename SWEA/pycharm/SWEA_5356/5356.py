import sys
sys.stdin = open('5356_input.txt')

def uiseok():
    ans = ''
    for j in range(15):
        for i in range(5):
            if j < len(words[i]):
                ans += words[i][j]
    return ans

T = int(input())
for tc in range(1, T+1):
    words = [list(input()) for _ in range(5)]
    print(f'#{tc} {uiseok()}')