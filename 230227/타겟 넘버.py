def solution(numbers, target):
    cnt = 0
    N = len(numbers)

    def dfs(i, numbers, summ):
        nonlocal cnt
        # 가지치기
        if i == N and summ == target:
            cnt += 1
            return
        if i == N:
            return

        dfs(i + 1, numbers, summ + numbers[i])  # 양수일 경우
        dfs(i + 1, numbers, summ - numbers[i])  # 음수일 경우

    dfs(0, numbers, 0)

    return cnt