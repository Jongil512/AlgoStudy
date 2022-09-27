N = int(input())
for tc in range(N):
    R, word = map(str, input().split())
    for i in range(len(word)):
        for j in range(int(R)):
            print(word[i], end='')