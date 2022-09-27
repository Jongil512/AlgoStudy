def solution(s):
    match = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    word = ''

    for i in range(len(s)):
        if s[i].isdigit():
            word += s[i]
        else:
            if s[i:i + 3] in match:
                word += str(match[s[i:i + 3]])
            elif s[i:i + 4] in match:
                word += str(match[s[i:i + 4]])
            elif s[i:i + 5] in match:
                word += str(match[s[i:i + 5]])

    answer = int(word)

    return answer

#   s = "one4seveneight"
#   result = 1478