import sys
sys.stdin = open('input.txt')

def change(m, n):
    if int(m) > int(n):
        return -1
    else:
        global cnt
        n_lst = list(n)
        flag = 1

        while flag:
            if n_lst[-1] == '1':
                n_lst = n_lst[:-1]
                cnt += 1
            else:
                flag = 0
        n = ''.join(n_lst)
        n = int(n) // 2
        cnt += 1
        if n == int(m):
            return cnt + 1
        elif n < int(m):
            cnt = -1
        change(m, str(n))

    return cnt + 1

M, N = map(str, input().split())
cnt = 0
print(change(M, N))