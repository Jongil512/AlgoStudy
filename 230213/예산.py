def solution(d, budget):
    d.sort()
    ssum = 0
    cnt = 0

    for num in d:
        if ssum + num > budget:
            return cnt
        cnt += 1
        ssum += num

    return cnt