from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    # deque를 활용해 일반 pop보다 시간 복잡도를 줄임
    q = deque(people)

    while len(q) > 1:
        # 몸무게가 가장 적은 사람과 큰 사람의 합이 limit 보다 적으면 두 사람을 태우고
        # 그렇지 않으면 몸무게가 가장 큰 사람만 태우고 감
        if q[0] + q[-1] <= limit:
            q.popleft()
        answer += 1
        q.pop()

    # 마지막 남은 사람이 있다면 결과 + 1
    if len(q):
        answer += 1

    return answer