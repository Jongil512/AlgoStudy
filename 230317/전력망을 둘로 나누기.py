from collections import deque

def solution(n, wires):
    # 그래프에 간선 정보 입력
    graph = [[] for _ in range(n + 1)]
    for w1, w2 in wires:
        graph[w1].append(w2)
        graph[w2].append(w1)

    def bfs(v):
        # 시작 간선 개수 1부터 시작
        cnt = 1
        # 방문 배열 초기화
        visited = [0] * (n + 1)
        # 방문 처리
        visited[v] = 1
        q = deque([v])
        while q:
            t = q.popleft()
            # t 와 연결되어있는 간선 찾기
            for w in graph[t]:
                # t와 연결되어있고 방문한 적이 없다면
                if not visited[w]:
                    # 큐에 추가, 방문 처리, cnt + 1
                    q.append(w)
                    visited[w] = 1
                    cnt += 1
        return cnt

    # 정답은 간선의 최대 개수보다 클 수 없음
    answer = n
    for w1, w2 in wires:
        # 순서대로 간선 제거
        graph[w1].remove(w2)
        graph[w2].remove(w1)

        # 제거한 간선의 양 숫자로 bfs를 돌려 나온 cnt 차이의 절댓값과 answer 비교
        answer = min(answer, abs(bfs(w1) - bfs(w2)))

        # 간선 다시 연결
        graph[w1].append(w2)
        graph[w2].append(w1)

    return answer