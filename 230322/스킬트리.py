def solution(skill, skill_trees):
    answer = 0
    # 중복이 업음
    # 스킬트리에서 하나씩 꺼내서 skill 안에 있는 문자만 추출
    for tree in skill_trees:
        start = ''.join([word for word in tree if word in skill])
        # skill이 추출한 문자열로 시작하면 올바른 스킬트리
        if skill.startswith(start):
            answer += 1
    return answer