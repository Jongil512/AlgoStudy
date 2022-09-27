import sys
sys.stdin = open('3499_input.txt')

def perfect_s(words):
    even_list = []
    odd_list = []
    new_list = []
    for i in range(N):
        if N % 2 == 1:
            if i <= N//2:
                odd_list.append(words[i])
            else:
                even_list.append(words[i])
        else:
            if i <= N//2 - 1:
                odd_list.append(words[i])
            else:
                even_list.append(words[i])
    for i in range(N//2):
        new_list.append(odd_list[i])
        new_list.append(even_list[i])
    if N % 2 == 1:
        new_list.append(odd_list[-1])
    return new_list

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    words = list(map(str, input().split()))
    print(f'#{tc}', *perfect_s(words))