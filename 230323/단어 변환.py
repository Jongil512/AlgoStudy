def solution(begin, target, words):
    global answer, flag
    # 최소값을 찾기 위해 큰 수로 초기화
    answer = 99999999
    N = len(begin)
    M = len(words)
    # 목표하는 단어를 찾은 여부
    flag = 0
    # 해당 단어 사용 여부
    used = [0] * M
    if target not in words:
        return 0

    def dfs(s, cnt):
        global answer, flag
        # 목표한 단어를 찾으면 최소값 비교 후 저장 및 flag 1로
        if s == target:
            answer = min(answer, cnt)
            flag = 1
            return
        # 단어를 하나씩 비교
        for w in range(M):
            dif = 0
            nw = ''
            for i in range(N):
                # 글자 차이가 나면 연산
                if s[i] != words[w][i]:
                    dif += 1
                    nw = words[w]
            # 만약 1글자만 차이나고 사용한 적이 없다면 사용표시 후 dfs
            if dif == 1 and not used[w]:
                used[w] = 1
                dfs(nw, cnt+1)
                # dfs가 끝났으니 사용 표시 제거
                used[w] = 0

    dfs(begin, 0)

    return answer if flag else 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))