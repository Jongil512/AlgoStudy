def solution(n):
    answer = []
    while True:
        if n >= 3:
            r, q = divmod(n, 3)
            answer.append(q)
            n = r
        else:
            answer.append(n)
            break
    answer = answer[::-1]
    for i in range(len(answer)-1, 1, -1):
        if answer[i] == 0:
            if answer[i - 1] == 0:
                continue
            else:
                answer[i - 1] -= 1
                answer[i] = 3

    return answer

# print(solution(1))
# print(solution(2))
# print(solution(3))
# print(solution(4))
# print(solution(5))
# print(solution(6))
# print(solution(7))
print(solution(12))
print(solution(14))
print(solution(27))