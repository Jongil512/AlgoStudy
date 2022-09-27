"""
DFS
"""

# DFS - 재귀
def dfs_recursive(vtx):
	global recur_cnt    # 재귀함수 호출된 횟수 저장 변수
	recur_cnt += 1

	visited[vtx] = 1    # 방문처리
	print(vtx, end=' ')
	for w in range(1, V + 1):
		if matrix[vtx][w] == 1 and visited[w] == 0:
			dfs_recursive(w)


# 인접 행렬 생성
def adj_matrix(e, arr):
	for i in range(e):
		v1, v2 = arr[i * 2], arr[i * 2 + 1]
		matrix[v1][v2] = 1
		matrix[v2][v1] = 1


V, E = map(int, input().split())    # 7 8
matrix = [[0] * (V + 1) for _ in range(V + 1)]
tmp = list(map(int, input().split()))       # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
adj_matrix(E, tmp)

recur_cnt = 0   # 재귀함수 호출된 횟수 저장 변수
visited = [0] * (V + 1)
dfs_recursive(1)
print('\n', recur_cnt)



