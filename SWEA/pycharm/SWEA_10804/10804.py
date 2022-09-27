import sys
sys.stdin = open('10804_input.txt')

def mirror():
    ans = []
    for i in word:
        if i == 'b':
           ans.insert(0, 'd')
        elif i == 'p':
           ans.insert(0, 'q')
        elif i == 'd':
           ans.insert(0, 'b')
        elif i == 'q':
           ans.insert(0, 'p')
    return ''.join(ans)

T = int(input())
for tc in range(1, T+1):
    word = input()
    print(f'#{tc} {mirror()}')