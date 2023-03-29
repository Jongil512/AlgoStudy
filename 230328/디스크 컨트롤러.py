import heapq

def solution(jobs):
    answer, cnt, now = 0, 0, 0
    l = len(jobs)
    jobs.sort()
    heap = []

    # cnt가 jobs의 길이보다 작으면 반복
    while cnt < l:
        # 작업이 남아있다면
        while jobs:
            # 현재 시간보다 먼저 들어온 요청을 heapq에 push
            # 다만 작업시간을 기준으로 오름차순 정렬이 필요하기 때문에 뒤집어서 넣음
            if jobs[0][0] <= now:
                heapq.heappush(heap, jobs.pop(0)[::-1])
            else:
                break

        # 만약 처리해야 할 작업이 있다면
        if heap:
            # 계산 후 cnt+1
            job = heapq.heappop(heap)
            now += job[0]
            answer += now - job[1]
            cnt += 1
        # 처리해야 할 작업이 없다면 now+1
        else:
            now += 1

    return int(answer / l)