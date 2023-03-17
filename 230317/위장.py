def solution(clothes):
    answer = 1
    dic = {}
    # 의상을 입지 않는 경우도 있기 때문에 시작 숫자는 2
    # 부위에 해당하는 수 + 1
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]] += 1
        else:
            dic[cloth[1]] = 2
    # 경우의 수 모두 곱한 다음
    for v in dic.values():
        answer *= v
    # 아무것도 입지 않는 경우를 제외하기 위해 -1
    return answer - 1