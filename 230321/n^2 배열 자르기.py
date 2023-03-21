def solution(n, left, right):
    answer = []
    # 첫 풀이는 문제 순서대로 구현함 (시간초과)
    #     matrix = [[0]*n for _ in range(n)]
    #     for i in range(n):
    #         for j in range(n):
    #             if i >= j:
    #                 matrix[i][j] = i+1
    #             elif i < j:
    #                 matrix[i][j] = j+1
    #     for lst in matrix:
    #         answer += lst

    #     return answer[left:right+1]

    # 규칙성을 찾음
    # idx를 n으로 나눈 (몫, 나머지)가 (행, 열)과 동일
    # 문제의 숫자는 1부터 시작하므로 +1
    for i in range(left, right + 1):
        k, t = divmod(i, n)
        answer.append(max(k, t) + 1)

    return answer

print(solution(5, 0, 7))