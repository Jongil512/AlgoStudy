# 항구에 들어오는 배

import sys
sys.stdin = open('4371_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    