import sys
from itertools import permutations

def left(entry, dist):
    global grid, cnt

    if entry - dist > 0 and not grid[entry - dist]:
        grid[entry-dist] = dist + 1
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

    # 어느 출입문을 먼저 여는지 결정
    for turn in permutations(range(3), 3):

        # 왼쪽, 오른쪽 방향 결정
        for way in range(2):
            def1, def2 = ways[way]

            # 낚시터 개수 만큼 배열 생성
            grid = [0]*(N+1)

            # 낚시꾼 자리 배치
            for i in turn:
                entry, fisher = info[i]

                # 출입구 위치가 비었는지 파악
                if grid[entry]:
                    cnt = 0
                else:
                    grid[entry] = 1
                    cnt = 1

                # 낚시꾼들이 모두 자리잡을 때까지 반복
                dist = 1
                while cnt < fisher:
                    def1(entry, dist)

                    if cnt == fisher:
                        break

                    def2(entry, dist)

                    dist += 1

            answer = min(answer, sum(grid))

    print(f'#{tc} {answer}')