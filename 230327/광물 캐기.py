def solution(picks, minerals):
    answer = 0

    mine = {
        "diamond": 0,
        "iron": 1,
        "stone": 2
    }

    cd = [[1, 1, 1],
          [5, 1, 1],
          [25, 5, 1]]

    # 총 곡괭이 수
    m = sum(picks)

    # 광물의 수가 총 곡괭이*5보다 크면 곡괭이*5만큼 슬라이싱
    if len(minerals) >= m * 5:
        minerals = minerals[:m * 5]

    # 광물을 5개씩 나누고 각 광물이 몇 개씩 있는지 체크
    lst = []
    tmp = [0, 0, 0]
    for i in range(len(minerals)):
        if i != 0 and i % 5 == 0:
            lst.append(tmp)
            tmp = [0, 0, 0]
        tmp[mine[minerals[i]]] += 1
    if tmp:
        lst.append(tmp)

    # 위에서 슬라이싱으로 곡괭이가 부족해서 광물을 못캐는 경우는 없으니 광물을 다이아 > 철 > 돌이 많은 순으로 정렬
    lst.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    # 정렬한 광물을 순회하며 각 곡괭이에 따른 피로도 누적
    for target in lst:
        if picks[0]:
            picks[0] -= 1
            answer += sum(target)
        elif picks[1]:
            picks[1] -= 1
            answer += target[0] * 5 + target[1] + target[2]
        elif picks[2]:
            picks[2] -= 1
            answer += target[0] * 25 + target[1] * 5 + target[2]
        else:
            break

    return answer

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))