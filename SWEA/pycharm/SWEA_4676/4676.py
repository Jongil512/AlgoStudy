import sys
sys.stdin = open('4676_input.txt')

def insert_hp():
    arr.sort()
    for i in range(H):
        word.insert(arr[i]+i, '-')
    return ''.join(word)

T = int(input())
for tc in range(1, T+1):
    word = list(input())
    L = len(word)
    H = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc}', insert_hp())