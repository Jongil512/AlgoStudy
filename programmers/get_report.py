def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {x: 0 for x in id_list}

    for rep in set(report):
        a, b = rep.split(' ')
        reported[b] += 1

    for rep in set(report):
        a, b = rep.split(' ')
        if reported[b] >= k:
            answer[id_list.index(a)] += 1

    return answer

#   id_list = ["muzi", "frodo", "apeach", "neo"]
#   report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#   k = 2
#   result = [2,1,1,0]