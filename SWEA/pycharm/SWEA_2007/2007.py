import sys

sys.stdin = open('2007_input.txt')

def rep_str(arr):
    # 문자열을 for문으로 돌림
    for i in range(1, 11):
        if arr[:i] == arr[i:i*2]:
            return i

T = int(input())
for tc in range(1, T+1):
    ques = input()
    print(f'#{tc} {rep_str(ques)}')