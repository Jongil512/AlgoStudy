# 삼성시의 버스 노선

import sys
sys.stdin = open('6485_input.txt')

def bus(a, b):
    for i in range(a, b+1):
        visited[i] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [0] * (5001)
    for i in range(N):
        A, B = map(int, input().split())
        bus(A, B)
    P = int(input())
    print(f'#{tc}', end=' ')
    for i in range(P-1):
        print(visited[int(input())], end=' ')
    print(visited[int(input())])