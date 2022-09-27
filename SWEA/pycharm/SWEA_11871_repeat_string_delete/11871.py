import sys
sys.stdin = open('11871_input.txt')

def del_rep_str(a):
    # top = 0
    # stack = [a[0]]
    # for i in range(1, len(a)):
    #     stack.append(a[i])
    #     top += 1
    #     if len(stack) >= 2:
    #         if stack[top-1] == a[i]:
    #             stack.pop()
    #             stack.pop()
    #             top -= 2
    # if top < 0:
    #     return 0
    # else:
    #     return len(stack)

    stack = []
    for i in range(len(a)):
        if not stack:
            stack.append(a[i])
        else:
            if stack[-1] == a[i]:
                stack.pop()
            else:
                stack.append(a[i])
    return len(stack)

T = int(input())
for tc in range(1, T+1):
    a = input()
    print(f'#{tc} {del_rep_str(a)}')