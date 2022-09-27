import sys
sys.stdin = open('1231_input.txt')

def in_order(vtx):
    if vtx:
        in_order(int(tree[vtx][1]))
        word.append(tree[vtx][0])
        in_order(int(tree[vtx][2]))

T = 10
for tc in range(1, T+1):
    V = int(input())
    tree = [[0] * 4 for _ in range(V+1)]                    # 알파벳, 왼쪽 자식, 오른쪽 자식, 부모
    info = [input().split() + [0] * 2 for _ in range(V)]    # 길이 4로 맞춤
    for i in range(V):                                      # 각각의 요소를 tree에 저장
        tree[i + 1][0] = info[i][1]
        tree[i + 1][1] = info[i][2]
        tree[i + 1][2] = info[i][3]
        tree[i + 1][3] = info[i][0]
    word = []                                               # 빈 문자열 생성
    in_order(1)
    print(f'#{tc}', ''.join(word))