import sys
sys.stdin = open('11764_input.txt')

def truck():
    global ans
    kg.sort(reverse=True)
    much.sort(reverse=True)
    j = 0
    for i in range(len(kg)):
        if kg[i] > much[j]:
            pass
        else:
            ans += kg[i]
            j += 1
            if j == len(much):
                break
    return ans

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0
    kg = list(map(int, input().split()))
    much = list(map(int, input().split()))
    print(f'#{tc} {truck()}')