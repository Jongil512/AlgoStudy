from itertools import permutations

def solution(user_id, banned_id):
    answer = []

    # 두 사용자 닉네임 비교
    def check(s1, s2):
        if len(s1) != len(s2):
            return False
        for j in range(len(s1)):
            if s2[j] == '*':
                continue
            if s1[j] != s2[j]:
                return False
        return True

    m = len(banned_id)
    # 불량 사용자 수에 따라 가능한 조합 모두 구함
    for perm in permutations(user_id, m):
        flag = True
        # 해당 조합들을 모두 불량 사용자 아이디와 비교
        for i in range(m):
            # 하나라도 맞지 않으면 flag는 False
            if not check(perm[i], banned_id[i]):
                flag = False
        # 만약 둘 다 일치한다면 set을 통해 answer내에 같은 조합이 존재하는지 판단 후 append
        if flag:
            if set(perm) not in answer:
                answer.append(set(perm))

    return len(answer)