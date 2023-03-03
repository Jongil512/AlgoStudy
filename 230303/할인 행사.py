# 1
def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        check = discount[i:i+10]
        right = 0
        for j in range(len(want)):
            if check.count(want[j]) != number[j]:
                right = 0
                break
            else:
                right += 1
        if right == len(want):
            answer += 1
    return answer


# 2
from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    # 딕셔너리화
    for i in range(len(want)):
        dic[want[i]] = number[i]

    # 슬라이싱 후 개수 비교
    for i in range(len(discount) - 9):
        if dic == Counter(discount[i:i + 10]):
            answer += 1

    return answer