import sys
sys.stdin = open('11688_input.txt')

def wilf_tree():
    a = b = 1
    for i in range(len(order)):
        if order[i] == 'L':
            b = a + b
        else:
            a = a + b
    return a, b

T = int(input())
for tc in range(1, T+1):
    order = list(input())
    print(f'#{tc}', *wilf_tree())