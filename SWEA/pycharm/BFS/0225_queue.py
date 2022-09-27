# N = 10
# SIZE = N * N * N
# Q = [0] * SIZE
# f, r = -1


# front, rear = -1, -1
# Q = [0] * 10
# rear += 1
# Q[rear] = 1
# rear += 1
# Q[rear] = 2
#
# front += 1
# print(Q[front])
# front += 1
# print(Q[front])

from collections import deque

p = deque()

p.append(1)
p.append(2)
p.append(3)

while p:
    print(p.popleft())
