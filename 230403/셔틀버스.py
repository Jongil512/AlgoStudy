def solution(n, t, m, timetable):
    answer = 0

    # 시간을 분으로
    def to_m(s):
        h, m = s.split(':')
        ssum = int(h) * 60 + int(m)
        return ssum

    # 분을 시간으로
    def to_h(num):
        h, m = divmod(num, 60)
        if h // 10 == 0:
            h = f"0{h}"
        if m // 10 == 0:
            m = f"0{m}"
        return f"{h}:{m}"

    # 시간순으로 정렬 후 분으로 변경
    timetable.sort()
    for i in range(len(timetable)):
        timetable[i] = to_m(timetable[i])

    # 현재 시간과 막차 시간 설정
    now = 540 - t
    end = 540 + t*(n-1)

    lastTime = 0
    # 버스 배차 횟수만큼 반복
    for i in range(n):
        now += t
        curNumInBus = 0
        # 아직 인원이 남아있고 현재 버스 탑승 인원 수가 정원보다 적으면 반복
        while len(timetable) and curNumInBus < m:
            # 가장 빠른 순서의 탑승 시간이 현재 이하면
            if timetable[0] <= now:
                # 탑승, 마지막 탑승 시간 갱신
                curNumInBus += 1
                lastTime = timetable.pop(0)
            else:
                break
    # 모든 배차 횟수만큼 반복했을 때
    # 현재 탑승 인원이 정원보다 적으면
    if curNumInBus < m:
        # 막차 시간에 탑승
        answer = end
    # 현재 탑승 인원이 최대면
    # 마지막 탑승한 사람보다 1분 빠르게 탑승
    elif curNumInBus == m:
        answer = lastTime - 1

    return to_h(answer)

print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))