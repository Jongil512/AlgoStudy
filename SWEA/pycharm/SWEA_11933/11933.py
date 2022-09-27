import sys
sys.stdin = open('11933_input.txt')

def sum_node(num):
    if num < N:
        sum_node(num * 2)
        sum_node(num * 2 + 1)
        if (num * 2 + 1) <= N:      # 자식 노드 2개
            tree[num] = tree[num * 2] + tree[num * 2 + 1]
        elif (num * 2) <= N:        # 자식 노드 1개
            tree[num] = tree[num * 2]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for i in range(M):
        node, value = map(int, input().split())
        tree[node] = value
    num = 1
    sum_node(num)
    print(f'#{tc} {tree[L]}')