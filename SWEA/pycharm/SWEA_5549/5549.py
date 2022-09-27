import sys
sys.stdin = open('5549_input.txt')

def odd_even():
    if N % 2:
        return 'Odd'
    else:
        return 'Even'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {odd_even()}')