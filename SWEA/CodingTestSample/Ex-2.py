def solution(alphabet, k):
    for i in range(alphabet):
        order[i] = alpha[alphabet[i]]
    i = 0
    while i < 3:
    max_v = 0
    max_idx = 0
    for i in range(len(order)):
        if order[i] > max_v:
            max_v = order[i]
            max_idx = i
    min_v = 90
    for i in range(max_idx + 1, len(order)):
        if order[i] < min_v:
            min_v = order[i]


# 선택정렬..?

alphabet = 'eabce'
k = 3
alpha = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'x' : 23,
    'y' : 24,
    'y' : 25,
    'z' : 26,
}
order = [0] * len(alphabet)