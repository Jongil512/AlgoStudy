# 공연 기획

import sys
sys.stdin = open('4789_input.txt')

def clap():
    aud = 0
    cnt = 0

    for i in range(len(S)-1):
        aud += int(S[i])
        if aud < i+1:
            cnt += (i+1) - aud
            aud += (i+1) - aud
    return cnt

T = int(input())
for tc in range(1, T+1):
    S = input()
    print(f'#{tc} {clap()}')