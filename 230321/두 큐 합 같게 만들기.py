from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    sq1, sq2 = sum(q1), sum(q2)
    # 두 큐의 합이 다르면 반복
    while sq1 != sq2:
        # 큐의 길이가 최대 300000이기 때문에 이 이상 반복시 -1 리턴
        if answer > 300000:
            return -1
        # 큐의 합이 큰 쪽에서 작은 쪽으로 인서트
        # while문 안에서 sum() 함수를 쓰지 않고 변수에 더해주는 식으로 진행
        if sq1 > sq2:
            t = q1.popleft()
            q2.append(t)
            sq1 -= t
            sq2 += t
            answer += 1
        else:
            t = q2.popleft()
            q1.append(t)
            sq2 -= t
            sq1 += t
            answer += 1

    return answer