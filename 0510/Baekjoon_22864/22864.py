import sys
sys.stdin = open('22864_input.txt')

def burnout():
    if A > M:
        return 0
    flag = 1
    tired = 0
    working_hours = 0
    rest_hours = 0
    while flag:
        if tired + A <= M:
            tired += A
            working_hours += 1
        else:
            r = tired - (M - A)
            if r % C:
                h = r // C + 1
            else:
                h = r // C
            tired -= C * h
            if tired < 0:
                tired = 0
            rest_hours += h
        if working_hours + rest_hours >= 24:
            flag = 0
    ans = working_hours * B
    return ans

A, B, C, M = map(int,input().split())
print(burnout())