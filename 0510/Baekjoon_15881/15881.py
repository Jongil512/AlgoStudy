def pPAp(word):
    cnt = 0
    i = 0
    while len(word) > 4:
        sample = word[:4]
        if sample == 'pPAp':
            cnt += 1
            word = word[4:]
        else:
            word = word[1:]
    return cnt

N = int(input())
word = input()
print(pPAp(word))
