import sys
sys.stdin = open('13229_input.txt')

def week():
    weeks = [0, 'SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON', 'SUN']
    ans = weeks.index(S)
    return ans

T = int(input())
for tc in range(1, T+1):
    S = input()
    print(f'#{tc} {week()}')