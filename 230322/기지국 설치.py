import math

def solution(n, stations, w):
    answer = 0
    idx = 1

    for st in stations:
        if st - w > 0:
            answer += math.ceil((st - w - idx) / (w * 2 + 1))
        idx = st + w + 1
    if idx <= n:
        answer += math.ceil((n - idx + 1) / (w * 2 + 1))

    return answer

print(solution(16, [1, 16], 2))