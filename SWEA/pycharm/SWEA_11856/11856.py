import sys
sys.stdin = open('11856_input.txt')

def judge():
    flag = 0
    for i in range(len(word)):
        if word.count(word[i]) != 2:
            flag = 1
    if flag:
        return 'No'
    return 'Yes'

T = int(input())
for tc in range(1, T+1):
    word = input()
    print(f'#{tc} {judge()}')