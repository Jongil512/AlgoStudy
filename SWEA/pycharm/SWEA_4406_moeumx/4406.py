import sys
sys.stdin = open('4406_input.txt')

def remove_moeum(a):
    moeum_list = ['a', 'e', 'i', 'o', 'u']
    ans = ''
    for i in range(len(a)):
        if a[i] in moeum_list:
            pass
        else:
            ans += a[i]
    return ans

T = int(input())
for tc in range(1, T+1):
    a = input()
    print(f'#{tc} {remove_moeum(a)}')