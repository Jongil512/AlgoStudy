import sys
sys.stdin = open('4047_input.txt')

def counting():
    # 문자열 분할해서 담을 리스트
    sep = ''
    cnt = 0
    # 각 문자열을 3자리씩 분할
    for i in range(len(kind)):
        sep += kind[i]
        cnt += 1
        if cnt == 3:
            lst.append(sep)
            sep = ''
            cnt = 0
    # 분할한 문자에서 각 문자에 맞는 개수 -1
    for i in range(len(lst)):
        # 만약 중복으로 있다면 에러
        if lst[i] in new_lst:
            return ['ERROR']
        else:
            new_lst.append(lst[i])
            if lst[i][0] == 'S':
                res[0] -= 1
            elif lst[i][0] == 'D':
                res[1] -= 1
            elif lst[i][0] == 'H':
                res[2] -= 1
            elif lst[i][0] == 'C':
                res[3] -= 1
    return res

T = int(input())
for tc in range(1, T+1):
    kind = input()
    lst = []
    new_lst = []
    res = [13, 13, 13, 13]
    print(f'#{tc}', *counting())