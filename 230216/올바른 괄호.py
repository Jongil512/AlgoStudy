def solution(s):
    answer = True
    q = []
    cnt = 0

    for w in s:
        if w == '(':
            q.append(w)
            cnt += 1
        else:
            if cnt > 0:
                q.pop()
                cnt -= 1
            else:
                return False

    return True if len(q) == 0 else False