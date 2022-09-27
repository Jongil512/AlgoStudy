import sys
sys.stdin = open('4408_input.txt')

def return_room(n):
    max_cnt = 1
    for i in range(n):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        new_s = (s+1)//2
        new_e = (e+1)//2
        for j in range(new_s, new_e + 1):
            cnt[j] += 1
            if cnt[j] > max_cnt:
                max_cnt = cnt[j]
    return max_cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = [0] * (200+1)
    print(f'#{tc} {return_room(N)}')