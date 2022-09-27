import sys
sys.stdin = open('5515_input.txt')

T = int(input())
for tc in range(1, T+1):
    m, d = map(int, input().split())
    month = {
        1 : 0,
        2 : 31,
        3: 60,
        4: 91,
        5: 121,
        6: 152,
        7: 182,
        8: 213,
        9: 244,
        10: 274,
        11: 305,
        12: 335
    }
    week = [3, 4, 5, 6, 0, 1, 2]
    ans = week[(month[m] + d) % 7]
    print(f'#{tc} {ans}')
