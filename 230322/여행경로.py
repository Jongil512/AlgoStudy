# 1
# dictionary로 담은 후 알파벳순 정렬, 비교하며 차례대로 answer에 넣기
# but 이렇게 하니 티켓 중복이 있고 후순위 알파벳에 다시 원래로 돌아오는 티켓인 경우 모든 티켓을 소비할 수 없게 됨
def solution(tickets):
    answer = ['ICN']
    nations = {x[0]:[] for x in tickets}
    for ticket in tickets:
        nations[ticket[0]].append(ticket[1])
    for v in nations.values():
        v.sort()
    start = 'ICN'
    def travle(s):
        if s in nations.keys() and nations[s]:
            nt = nations[s][0]
            answer.append(nt)
            nations[s].pop(0)
            travle(nt)
        else:
            return
    travle(start)
    return answer

# 2
# 티켓 목적지별로 정렬하되 역순으로 정렬
# DFS 방식으로 하나씩
from collections import deque

def solution(tickets):
    tickets.sort(key=lambda x:x[1], reverse=True)
    nations = {x[0]:[] for x in tickets}
    for ticket in tickets:
        nations[ticket[0]].append(ticket[1])
    q = deque(['ICN'])
    path = []
    while q:
        t = q[-1]

        if t not in nations or not nations[t]:
            path.append(q.pop())
        else:
            q.append(nations[t][-1])
            nations[t] = nations[t][:-1]

    return path[::-1]