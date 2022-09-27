import sys
sys.stdin = open('10570_input.txt')

def palindrome2(a, b):
    cnt = 0
    for i in range(1, 34):
        if a <= (i**2) <= b:
            if i < 10:
                if (i ** 2) < 10:
                    cnt += 1
                elif str(i ** 2)[0] == str(i ** 2)[1]:
                    cnt += 1
            if i >= 10:
                if str(i)[0] == str(i)[1] and str(i ** 2)[0] == str(i ** 2)[2]:
                    cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    print(f'#{tc} {palindrome2(A, B)}')