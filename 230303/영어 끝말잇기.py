#1
def solution(n, words):
    answer = [0, 1]
    # 확인한 단어
    check = [words[0]]
    # 진행 횟수
    cnt = 1
    # 순서
    order = 0
    for i in range(1, len(words)):
        check.append(words[i])
        cnt += 1
        order += 1
        # 진행 횟수가 사람 수를 넘으면 +1, cnt 초기화
        if cnt > n:
            answer[1] += 1
            cnt = 1
        # 단어 끝말 비교
        # 이전에 등장했는지 확인
        post = words[i-1]
        later = words[i]
        if post[-1] != later[0] or check.count(later) >= 2:
            # 순서 체크
            answer[0] = (order%n)+1
            return answer
    return [0, 0]

#2
def solution(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    return [0, 0]