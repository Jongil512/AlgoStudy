import heapq as hq

def solution(n, s, a, b, fares):
    answer = float('inf')
    # 그래프 저장
    graph = [[] for _ in range(n + 1)]
    for sr, en, f in fares:
        graph[sr].append((en, f))
        graph[en].append((sr, f))

    def dijkstra(v):
        distance = [float('inf')] * (n + 1)
        distance[v] = 0
        q = []
        hq.heappush(q, (0, v))

        while q:
            dist, now = hq.heappop(q)

            if distance[now] < dist:
                continue

            for w in graph[now]:
                nd, nv = w[1], w[0]
                if distance[nv] > dist + nd:
                    distance[nv] = dist + nd
                    hq.heappush(q, (dist + nd, nv))
        return distance

    # 각 점마다 최단거리를 구한 후 해당 점에서 s, a, b까지의 거리 합과 기존 answer를 비교
    for i in range(1, n + 1):
        d = dijkstra(i)
        answer = min(answer, d[s] + d[a] + d[b])

    return answer