import sys
sys.stdin = open('5356_input.txt')

def uiseok(arr):
    ans = []
    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):
                ans.append(arr[i][j])
    return ''.join(ans)


T = int(input())
for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    print(f'#{tc}', uiseok(arr))