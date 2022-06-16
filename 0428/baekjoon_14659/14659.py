import sys
sys.stdin = open('14659_input.txt')

def hanzo():
    max_cnt = 0
    cnt = 0
    idx = 0
    for i in range(1, N):
        if arr[i] > arr[idx]:
            idx = i
            cnt = 0
        elif arr[i] < arr[idx]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
            if i == N-1:
                return max_cnt

    return max_cnt

N = int(input())
arr = list(map(int, input().split()))
print(hanzo())