from collections import deque

def mychew(N, np):
    while N > 0:                       # 마이쮸가 남아있는 동안
        num, cnt = q.pop(0)            # 줄의 맨 앞 사람과 이전에 받은 개수
        cnt += 1                       # 갯수 증가
        lp = num                       # 마지막으로 받은 사람 할당
        N -= cnt                       # 마이쮸 개수 감소
        np += 1                        # 새로운 사람 증가
        q.append((lp, cnt))
        q.append((np, 0))
        input()
        print(len(q), lp, N)


N = 20
q = [(1, 0)]        # (사람번호, 직전까지 받았던 개수)
new_people = 1      # 새롭게 줄을 서는 사람 번호
last_people = 0     # 마지막으로 받아간 사람
mychew(N, new_people)