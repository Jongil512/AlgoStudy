import heapq
from itertools import combinations

def solution(n, m, x, y, z):
    answer = []
    graph = [[] for _ in range(n+1)]
    route = [[[]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
    traffic = [[0]*(n+1) for _ in range(n+1)]

    for i, j, k in zip(x, y, z):
        graph[i].append([j, k])
        graph[j].append([i, k])

    def dijkstra(start):
        distance = [float('inf')] * (n+1)
        distance[start] = 0
        r = str(start)
        heap = []
        heapq.heappush(heap, (0, start, r))

        while heap:
            dist, node, way = heapq.heappop(heap)

            if distance[node] < dist:
                continue

            for neighbor, weight in graph[node]:
                new_dist = dist + weight

                if new_dist == distance[neighbor]:
                    distance[neighbor] = new_dist
                    route[start][neighbor].append(way + str(neighbor))
                    heapq.heappush(heap, (new_dist, neighbor, way + str(neighbor)))
                elif new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    route[start][neighbor] = [way + str(neighbor)]
                    heapq.heappush(heap, (new_dist, neighbor, way + str(neighbor)))

    for i in range(1, n+1):
        dijkstra(i)

    for s, e in combinations(range(1, n+1), 2):
        route[s][e].sort()
        l = len(route[s][e][-1])
        for road in route[s][e]:
            if len(road) == l:
                for i in range(len(road)-1):
                    traffic[int(road[i])][int(road[i+1])] += 1
                    traffic[int(road[i+1])][int(road[i])] += 1
                break

    tmp = []
    for idx, (s, e) in enumerate(zip(x, y)):
        tmp.append([traffic[s][e] + traffic[e][s], idx+1])
    tmp = sorted(tmp, key=lambda x:(-x[0], x[1]))

    for a in tmp:
        answer.append(a[1])

    return answer

print(solution(3, 3, [1, 1, 2], [3, 2, 3], [1, 5, 2]))
# return    [1, 3, 2]
print(solution(4, 4, [1, 1, 3, 4], [3, 4, 2, 2], [2, 1, 1, 2]))
# return    [1, 2, 3, 4]
print(solution(5, 5, [1, 1, 1, 2, 3], [2, 4, 5, 3, 4], [1, 2, 6, 11, 4]))
# return    [2, 1, 3, 5, 4]