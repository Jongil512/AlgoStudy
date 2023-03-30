def solution(n, times):
    answer = 0
    # 이분탐색 기본 조건 초기화
    # 최대는 6명 모두 최대 시간이 걸리는 경우
    left, right = 1, max(times) * n

    # 이분탐색 시작
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            # mid분 동안 각 감독관이 검사할 수 있는 사람 수
            people += mid // time
            # 만약 people이 주어진 인원보다 많으면 break
            if people >= n:
                break

        # mid분 동안 주어진 인원을 모두 검사하지 못했으면 left = mid+1
        if people < n:
            left = mid + 1
        # mid분 동안 주어진 인원 이상을 검사했다면
        # answer에 mid 저장
        # right = mid - 1
        else:
            answer = mid
            right = mid - 1

    return answer