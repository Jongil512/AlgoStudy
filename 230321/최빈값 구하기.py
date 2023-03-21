# 1
def solution1(array):
    cnt = []
    s_arr = list(set(array))
    answer = 0
    MAX = 0
    for num in s_arr:
        t = array.count(num)
        cnt.append(t)
        if MAX < t:
            MAX = t
            answer = num
    if cnt.count(max(cnt)) > 1:
        return -1
    return answer

# 2
def solution2(array):
    # set의 숫자들을 순환하며 기존 array에서 삭제
    # 마지막 숫자 하나가 남는다면 그 숫자가 최빈값
    # 만약 idx가 2이상이라면 최빈값 중복되므로 -1 return
    while len(array):
        for idx, num in enumerate(set(array)):
            array.remove(num)
        if idx == 0: return num
    return -1

print(solution2([1, 2, 3, 3, 3, 4]))