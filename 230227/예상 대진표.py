def solution(n, a, b):
    answer = 0

    while a != b:
        answer += 1
        # a = 1, b = 2일 경우 값 동일
        # a = 2, b = 3일 경우 값 다름
        a, b = (a + 1) // 2, (b + 1) // 2

    return answer