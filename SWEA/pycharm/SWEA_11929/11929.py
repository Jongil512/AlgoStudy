import sys
sys.stdin = open('11929_input.txt')

def enq(n):
    global last
    last += 1
    tree[last] = n

    c = last
    p = c // 2
    while p and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

def ans():
    global last
    ans = 0
    while last != 0:
        ans += tree[last // 2]
        last = last // 2
    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] + (list(range(1, len(arr)+1)))
    last = 0
    for i in arr:
        enq(i)
    print(f'#{tc} {ans()}')