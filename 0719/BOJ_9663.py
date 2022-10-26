# N-Queen

import sys

def Queen(v):
    global cnt
    if v == N:
        cnt += 1
        return

    for i in range(N):
        if visited[i] == 0:     # 해당 자리에 퀸이 존재하는지 확인
            exist_queen[v] = i  # 각 행마다 위치하는 퀸의 자리

            temp = True
            for j in range(v):
                if abs(exist_queen[v] - exist_queen[j]) == abs(v - j):
                    temp = False
                    return

            if temp:
                visited[i] = 1
                Queen(v+1)
                visited[i] = 0


N = int(sys.stdin.readline().rstrip())
visited = [0]*N         # 퀸 존재 판별 배열
exist_queen = [0]*N     # 해당 행에 놓인 퀸의 위치

cnt = 0
Queen(0)
print(cnt)