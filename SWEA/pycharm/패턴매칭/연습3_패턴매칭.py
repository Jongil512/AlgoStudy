def brute_force(text, pattern):
    N = len(text)
    M = len(pattern)
    for i in range(N-M+1):
        flag = 1    # 패턴을 찾았을 때 값
        for j in range(M):
            if text[i+j] != pattern[j]:
                flag = 0    # 패턴을 찾지 못했을 때 값
                break    # for문 실행 도중
        # for문을 다 돌렸으면 flag = 1로 변화가 없다.
        if flag:
            return i
    return -1


text = 'a pattern matching algorithm'
pattern = 'rithm'
print(text.find(pattern))