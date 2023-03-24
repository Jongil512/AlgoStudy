def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(v):
        visited[v] = 1
        for (idx, c) in enumerate(computers[v]):
            if c and not visited[idx]:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))