import heapq

# 우선순위 큐를 사용해 쉽게 최솟값을 구해 연산 (일일이 정렬할 필요 x)
def solution(scoville, K):
    answer = 0
    # 우선순위큐로 만듦
    heapq.heapify(scoville)

    # 스코빌 리스트의 길이가 2 이상일 때만 연산이 가능하기에 while문 조건 설정
    while True:

        # 최솟값을 꺼내 목표치인 K와 비교
        # K 이상이라면 answer를
        # K 미만이지만 남은 리스트가 없다면 -1을 리턴
        m1 = heapq.heappop(scoville)
        if m1 >= K:
            return answer

        if not len(scoville):
            return -1

        # 최솟값이 K 미만이라면 연산을 위해 다음 최솟값을 꺼냄
        m2 = heapq.heappop(scoville)

        # 제시된 연산 실행
        rst = m1 + (m2 * 2)

        # 연산된 값을 다시 스코빌 리스트에 넣고 answer 값 +1
        heapq.heappush(scoville, rst)
        answer += 1