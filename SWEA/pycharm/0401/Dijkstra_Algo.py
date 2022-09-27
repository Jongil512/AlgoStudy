'''
서울(0), 천안(1), 원주(2), 논산(3), 대전(4),
대구(5), 강릉(6), 광주(7), 부산(8), 포항(9)

[0, 12, 15, 16, 19, 22, 36, 29, 31, 36]
'''
import sys
sys.stdin = open('Dijkstra.txt')

def Dijkstra(v):
    # 출발점 선택
    dist[v] = 0
    # 모든 도시 선택될 때까지 반복
    for i in range(V):
        min = 9999999
        for w in range(V):
            if not visited[w] and dist[w] < min:
                min = dist[w]
                u = w   # 최소값의 인덱스
        # 최소값 도시의 방문체크
        visited[u] = 1
        # 최소값 도시에 인접하고 방문 안 한 도시 가중치 업데이트
        for w in range(V):
            if adj[u][w] and not visited[w]:
                if dist[w] > dist[u] + adj[u][w]:
                    dist[w] = dist[u] + adj[u][w]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())            # 정점 수, 간선 수
    adj = [[0] * V for _ in range(V)]   # 인접 행렬
    dist = [99999999] * V                         # 가중치
    visited = [0] * V                   # 방문 처리
    for i in range(E):
        s, e, d = map(int, input().split())
        adj[s][e] = adj[e][s] = d
    Dijkstra(0)
    print(dist)