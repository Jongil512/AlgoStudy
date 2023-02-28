import math

def solution(str1, str2):
    words1 = to_slice_and_upper(str1)
    words2 = to_slice_and_upper(str2)

    if words1 == [] and words2 == []:
        return 65536

    w1_copy = words1.copy()
    w2_copy = words2.copy()

    # 교집합
    inter = []
    for w in words1:
        if w in w2_copy:
            inter.append(w)
            w1_copy.remove(w)
            w2_copy.remove(w)

    # 합집합
    union = inter + w1_copy + w2_copy

    answer = math.floor((len(inter) / len(union)) * 65536)
    return answer


def to_slice_and_upper(s):
    s = s.upper()
    a = []
    for i in range(len(s) - 1):
        if s[i:i + 2].isalpha():
            a.append(s[i:i + 2])
    return a
