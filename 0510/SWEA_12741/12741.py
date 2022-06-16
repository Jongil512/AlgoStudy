import sys
sys.stdin = open('12741_input.txt')
# 두 전구
def bulb():
    if B - C < 1 or D - A < 1:
        answer.append(0)
    else:
        if A <= C:
            if B > D:
                answer.append(D - C)
            else:
                answer.append(B - C)
        else:
            if B > D:
                answer.append(D - A)
            else:
                answer.append(B - A)

answer = []
T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    bulb()
for i in range(T):
    print(f'#{i+1} {answer[i]}')