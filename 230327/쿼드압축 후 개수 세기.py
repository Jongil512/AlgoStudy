def solution(arr):
    global answer
    answer = [0, 0]
    n = len(arr)

    def divide(x, y, l):
        global answer
        # 길이가 1일 경우는 무조건 answer에 더해줌
        if l == 1:
            answer[arr[x][y]] += 1
            return
        target = arr[x][y]
        # 가장 큰 사각형부터 시작해 target과 다른 수가 나온다면 정사각형 4분할 후 다시 실행
        for i in range(x, x + l):
            for j in range(y, y + l):
                if arr[i][j] != target:
                    k = l // 2
                    divide(x, y, k)
                    divide(x + k, y, k)
                    divide(x, y + k, k)
                    divide(x + k, y + k, k)
                    return
        # target과 다른 적이 없으면 해당 숫자 카운트 +1
        answer[target] += 1

    divide(0, 0, n)
    return answer