from collections import deque

def solution(s):
    answer = 0
    q = deque()

    for i in range(0, len(s)):
        if not q:
            q.append(s[i])
        elif s[i] == q[-1]:
            q.pop()
        else:
            q.append(s[i])

    if not q:
        answer = 1

    return answer