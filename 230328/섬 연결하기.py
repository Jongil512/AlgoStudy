# 크루스칼 알고리즘을 통해 풀이
def solution(n, costs):
    answer = 0
    parent = [0] * n
    # 각자 자기 자신을 부모로 가짐
    for i in range(n):
        parent[i] = i
    costs.sort(key=lambda x: x[2])

    # 부모 찾기 (부모노드가 자기 자신이 아니라면 가장 최종 부모 노드를 저장)
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 노드의 부모를 비교해 더 작은 노드를 저장
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    for cost in costs:
        s, e, c = cost
        # 부모를 찾는 동시에 부모 노드 업데이트
        a = find_parent(parent, s)
        b = find_parent(parent, e)
        # 만약 부모 노드가 다르다면 싸이클이 없는 간선이기 때문에 연결
        if a != b:
            # 연결하며 부모 노드 업데이트
            union_parent(parent, s, e)
            answer += c

    return answer

print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))