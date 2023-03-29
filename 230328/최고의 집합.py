def solution(n, s):
    if n > s:
        return [-1]

    tmp, remainder = divmod(s, n)
    answer = [tmp] * n
    if remainder:
        for i in range(remainder):
            answer[i] += 1

    return sorted(answer)