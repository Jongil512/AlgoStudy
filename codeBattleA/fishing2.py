import sys
from itertools import permutations

def left(entry, dist):
    global grid, cnt

    if entry - dist > 0 and not grid[entry - dist]:
        grid[entry - dist] = dist + 1
        cnt += 1

def right(entry, dist):
    global grid, cnt

    if entry + dist <= N and not grid[entry + dist]:
        grid[entry + dist] = dist + 1
        cnt += 1

T = int(sys.stdin.readline().rstrip())
for tc in range(1, T+1):
    N = int(sys.stdin.readline().rstrip())
    info = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(3)]
    answer = float('inf')

    ways = [[left, right], [right, left]]
    for turn in permutations(range(3), 3):

        for way in range(2):
            def1, def2 = ways[way]

            grid = [0] * (N+1)

            for i in turn:
                entry, fisher = info[i]

                if grid[entry]:
                    cnt = 0
                else:
                    grid[entry] = 1
                    cnt = 1

                dist = 1

                while cnt < fisher:
                    def1(entry, dist)

                    if cnt == fisher:
                        break

                    def2(entry, dist)

                    dist += 1

            answer = min(answer, sum(grid))

    print(f'#{tc} {answer}')