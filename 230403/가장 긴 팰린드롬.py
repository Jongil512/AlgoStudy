def palin(s, left, right):
    # 팰린드롬 길이가 2인 경우
    if right - left == 1:
        l = 0
    # 팰린드롬 길이가 3인 경우
    else:
        l = 1
    while left >= 0 and right < len(s):
        # 두 문자열 비교, 같으면 양쪽+1 다시 비교
        if s[left] == s[right]:
            left -= 1
            right -= 1
            l += 2
        else:
            break
    return l


def solution(s):
    answer = 0
    if len(s) == 1:
        return 1

    for i in range(len(s) - 1):
        # 가장 짧은 팰린드롬이 성립되는 경우는 길이가 2인 경우, 길이가 3인 경우 (1인 경우는 가지치기)
        # 따라서 left, right의 기준을 두고 앞뒤 문자열을 비교해가며 answer를 갱신
        answer = max(answer, palin(s, i, i + 1), palin(s, i, i + 2))

    return answer

print(solution("abcdcba"))
# print(solution("abacde"))