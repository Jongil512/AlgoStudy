import sys
sys.stdin = open('1228_input.txt')

def update():
    i = 0
    cnt = 1
    while cnt <= M:
        if inse[i] == 'I':
            idx = int(inse[i+1])
            num = int(inse[i+2])
            cnt += 1
            for j in range(num):
                base.insert(idx + j, inse[i + 3 + j])
        i += 1

T = 10
for tc in range(1, T+1):
    N = int(input())
    base = list(map(int, input().split()))
    M = int(input())
    inse = list(map(str, input().split()))
    update()
    print(f'#{tc}', *base[:10])