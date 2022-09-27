def cnt_word(word, N):
    word_list = []
    for i in range(N):
        if word[i] not in word_list:
            word_list.append(word[i])
    cnt_word = []
    x = 0
    index = 0
    for i in range(len(word_list)):
        cnt_word.append(word.count(word_list[i]))
        if word.count(word_list[i]) > x:
            index = i
            x = word.count(word_list[i])
    cnt = 0
    for i in range(len(cnt_word)):
        if cnt_word[i] == x:
            cnt += 1
    if cnt > 1:
        return '?'
    else:
        return word_list[index].upper()

word = input().lower()
N = len(word)
print(cnt_word(word, N))