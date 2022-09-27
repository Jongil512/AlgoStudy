def solution(dartResult):
    answer = []

    # 알파벳 제곱순으로 나열
    score = ['S', 'D', 'T']

    # 숫자가 10일 경우를 대비해 A로 치환
    dartResult = dartResult.replace('10', 'A')

    # 치환한 문자열을 리스트로 변경 ( A 일때 10으로 )
    dart = ['10' if i == 'A' else i for i in dartResult]

    # 점수 인덱스로 활용
    i = -1

    for j in dart:
        # 만약 알파벳이면
        if j in score:
            # 해당 점수에 제곱
            answer[i] = answer[i] ** (score.index(j) + 1)
        # * 옵션이면
        elif j == '*':
            # 해당 점수 두 배
            answer[i] = answer[i] * 2
            # 첫 점수가 아닐 경우
            if i != 0:
                # 이전 점수도 2배
                answer[i - 1] = answer[i - 1] * 2
        # # 옵션이면
        elif j == '#':
            # 해당 점수 *(1)
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1

    return sum(answer)