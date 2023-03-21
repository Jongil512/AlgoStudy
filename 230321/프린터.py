def solution(priorities, location):
    answer = 0
    N = len(priorities)
    # 가장 큰 값의 index를 start로 시작
    start = priorities.index(max(priorities))
    # priorities[location]이 출력되면 종료
    while priorities[location]:
        # 최댓값과 현재 숫자가 같으면 출력
        if max(priorities) == priorities[start]:
            # 출력 시 수를 0으로 변경
            priorities[start] = 0
            # 출력횟수 및 index + 1
            answer += 1
            start += 1
        # 현재 숫자가 최댓값보다 작으면 다음 숫자로
        else:
            start += 1
        # 인덱스가 최대 범위 넘어가면 처음으로 초기화
        if start == N:
            start = 0

    return answer

print(solution([2, 1, 3, 2], 2))