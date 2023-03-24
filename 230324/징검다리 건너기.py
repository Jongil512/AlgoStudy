# 1 [무식하게 while문과 for문으로 돌림]
# 효율성 검사에서 실패
# def solution(stones, k):
#     answer = 0
#     N = len(stones)
#
#     flag = 1
#     i = -1
#     while flag:
#         check = 0
#         for j in range(1, k + 1):
#             if i + j > N - 1:
#                 answer += 1
#                 i = -1
#                 check = True
#                 break
#             elif stones[i + j]:
#                 if i + j == N - 1:
#                     answer += 1
#                     stones[i + j] -= 1
#                     i = -1
#                 else:
#                     stones[i + j] -= 1
#                     i += j
#                 check = 1
#                 break
#         if not check:
#             flag = 0
#
#     return answer

# 2 이진탐색 사용
# (최소값+최대값)//2 인 mid 값보다 작은 값이 연속 k번 이상 나오면 건널 수 없음 (mid = right -1)
# mid 값보다 큰 값이 연속 k번 이상 나오면 건널 수 있음 (mid = left + 1)
def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    while left <= right:
        flag = 1
        cnt = 0
        mid = (left + right) // 2
        for s in stones:
            if s < mid:
                cnt += 1
                if cnt == k:
                    flag = 0
                    break
            else:
                cnt = 0
        if flag:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))