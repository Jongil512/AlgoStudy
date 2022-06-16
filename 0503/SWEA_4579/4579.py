import sys
sys.stdin = open('4579_input.txt')


def palindrome(S):
    while len(S) > 1:
        if S[0] == '*' or S[-1] == '*':
            return 'Exist'
        if S[0] == S[-1]:
            S = S[1:-1]
        else:
            return 'Not exist'
    return 'Exist'


T = int(input())
for tc in range(1, T + 1):
    S = input()
    print(f'#{tc} {palindrome(S)}')