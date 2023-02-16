def solution(s):
    words = list(s)
    answer = ''
    to_add = ''

    for w in words:
        if w == ' ':
            answer = answer + to_add.capitalize() + ' '
            to_add = ''
        else:
            to_add += w

    answer += to_add.capitalize()

    return answer