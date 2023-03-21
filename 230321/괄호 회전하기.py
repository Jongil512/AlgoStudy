from collections import deque

def solution(s):
    lst = ['[]', '{}', '()']
    global answer
    answer = 0
    N = len(s)
    q = deque()

    def check_right(s, q):
        global answer
        for word in s:
            if q and q[-1] + word in lst:
                q.pop()
            else:
                q.append(word)
        if q:
            return
        else:
            answer += 1

    for i in range(N):
        new_s = s[i:] + s[:i]
        check_right(new_s, q)

    return answer

print(solution("[](){}"))