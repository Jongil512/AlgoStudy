from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    days = deque()

    for progress, speed in zip(progresses, speeds):
        dif = 100 - progress
        day = math.ceil(dif / speed)
        days.append(day)

    cnt = 1
    while len(days) > 1:
        t = days[0]
        if t >= days[1]:
            cnt += 1
            days.popleft()
        else:
            answer.append(cnt)
            cnt = 1
            days.popleft()
    answer.append(cnt)
    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# print(solution([93, 30, 55], 	[1, 30, 5]))