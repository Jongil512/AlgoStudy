# 세상의 모든 팰린드롬

import sys
sys.stdin = open('4522_input.txt')

def palindrome(S):
    # 조건을 만족하면 문자의 길이가 1이하가 될때까지 슬라이싱 반복
    while len(S) > 1:
        # 양쪽 문자가 같거나 하나라도 ? 이면 ㅇㅋ
        if S[0] == S[-1] or S[0] == '?' or S[-1] == '?':
            S = S[1:-1]
        else:
            # 조건에 부합하지 않으면 Not exist 출력
            return 'Not exist'
    return 'Exist'

T = int(input())
for tc in range(1, T+1):
    S = input()
    print(f'#{tc} {palindrome(S)}')