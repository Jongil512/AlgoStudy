import sys
sys.stdin = open('3142_input.txt')

def animal():
    global u, t
    u = M * 2 - N
    t = M - u

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    u = t = 0
    animal()
    print(f'#{tc} {u} {t}')