import heapq

def solution(n, works):
    answer = 0
    # 가지치기
    if sum(works) <= n:
        return 0
    # 기존 while 문을 사용하니 효율성 테스트 실패
    # heap 자료구조를 사용
    heap = []
    # 최대값을 먼저 빼야하니 -v를 넣어준다
    for v in works:
        heapq.heappush(heap, -v)

    cnt = 0
    while cnt < n:
        # -를 붙여 heap에 넣어줬으니 heappop 하면 최대값이 나옴
        t = heapq.heappop(heap)
        # 최대값 하나 줄이기
        t += 1
        # 다시 heap에 넣어줌
        heapq.heappush(heap, t)
        cnt += 1

    for he in heap:
        # -가 붙어있으나 제곱을 하므로 부호는 신경쓰지 않아도 됨
        answer += he ** 2

    return answer