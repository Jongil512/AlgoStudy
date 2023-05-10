def solution(S):
    def backtrack(i, curr_red, curr_blue):
        nonlocal cnt
        if i == len(S):
            if curr_red == curr_blue:
                cnt += 1
            return

        # 레드가 숫자를 먼저 말한 경우
        if len(curr_red) == len(curr_blue):
            # 레드가 숫자를 말한 경우
            if S[i].isdigit():
                new_red = curr_red + S[i]
                backtrack(i + 1, new_red, curr_blue)
            # 레드가 연산자를 말한 경우
            else:
                for op in "+-":
                    new_blue = curr_blue + op
                    backtrack(i, curr_red, new_blue)
        # 블루가 숫자를 먼저 말한 경우
        else:
            # 블루가 숫자를 말한 경우
            if S[i].isdigit():
                new_blue = curr_blue + S[i]
                backtrack(i + 1, curr_red, new_blue)
            # 블루가 연산자를 말한 경우
            else:
                for op in "+-":
                    new_red = curr_red + op
                    backtrack(i, new_red, curr_blue)

    cnt = 0
    backtrack(0, "", "")
    return cnt

print(solution("1111"))