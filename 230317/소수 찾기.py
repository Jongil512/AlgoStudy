from itertools import permutations
import math

def solution(numbers):
    answer = 0
    # 주어진 문자열 분할하여 리스트로
    nums = list(map(str, numbers))
    c_nums = []
    # 중복 허용하지 않기 위해 set 자료형 생성
    checks = set()
    # 만들 수 있는 모든 경우의 수 찾아서 리스트에 추가
    for i in range(1, len(nums) + 1):
        c_nums += permutations(nums, i)
    # 찾은 경우의 수를 중복 제거를 위해 자연수로 만들고 set에 추가
    for num in c_nums:
        checks.add(int(''.join(num)))
    # set을 돌며 소수 찾기
    for check in checks:
        flag = True
        if check <= 1:
            continue
        for i in range(2, int(math.sqrt(check)) + 1):
            if check % i == 0:
                flag = False
        if flag:
            answer += 1

    return answer