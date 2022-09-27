import sys
sys.stdin = open('1926_input.txt')

def thrsixnin(n):
    tsn_list = [3, 6, 9]
    ans_list = []
    for i in range(1, n + 1):
        cnt = 0
        if i % 10 in tsn_list:
            cnt += 1
            i //= 10
            if i % 10 in tsn_list:
                cnt += 1
                i //= 10
                if i % 10 in tsn_list:
                    cnt += 1
        if i // 10 in tsn_list:
            cnt += 1
        # if i % 100

        if cnt == 0:
            ans_list.append(i)
        if cnt == 1:
            ans_list.append('-')
        if cnt == 2:
            ans_list.append('--')
        if cnt == 3:
            ans_list.append('---')
    return ans_list


N = int(input())
print(thrsixnin(N))