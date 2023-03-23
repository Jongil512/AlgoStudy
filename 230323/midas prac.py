def solution(n, m, x, y, z):
    answer = []
    dijk = [[float("inf")]*(n+1) for _ in range(n+1)]
    bridge = [[]*(n+1) for _ in range(n+1)]
    involved = [[0]*(n+1) for _ in range(n+1)]
    route = []
    tmp = []
    for i, j, k in zip(x, y, z):
        bridge[i].append((j, k))
        bridge[j].append((i, k))

    def small_node(v):
        minn = float("inf")
        idx = 0
        for i in range(1, n+1):
            if dijk[v][i] < minn and not visited[i]:
                minn = dijk[v][i]
                idx = i
        return idx

    def dijkstra(v, r):
        r += str(v)
        dijk[v][v] = 0
        visited[v] = 1
        for e, w in bridge[v]:
            dijk[v][e] = w
            dijk[e][v] = w
            route.append(r+str(e))
        for _ in range(n-1):
            now = small_node(v)
            visited[now] = 1
            r += str(now)

            for j in bridge[now]:
                if not visited[j[0]] and dijk[v][now] + j[1] < dijk[v][j[0]]:
                    dijk[v][j[0]] = dijk[v][now] + j[1]
                    route.append(r + str(j[0]))

    for i in range(1, n+1):
        visited = [0] * (n + 1)
        r = ''
        dijkstra(i, r)

    for road in route:
        for i in range(len(road)-1):
            involved[int(road[i])][int(road[i+1])] += 1

    for idx, (s, e) in enumerate(zip(x, y)):
        tmp.append([involved[s][e], idx+1])

    tmp.sort(key=lambda x :(-x[0], x[1]))
    for t in tmp:
        answer.append(t[1])
    return answer

# print(solution(3, 3, [1, 1, 2], [3, 2, 3], [1, 5, 2]))
# return    [1, 3, 2]
# print(solution(4, 4, [1, 1, 3, 4], [3, 4, 2, 2], [2, 1, 1, 2]))
# return    [1, 2, 3, 4]