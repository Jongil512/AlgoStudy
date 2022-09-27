import sys
sys.stdin = open('11870_input.txt')

def judge_bracket(a):
    top = -1
    stack = []
    for i in a:
        if i == '(' or i == '{':
            stack.append(i)
            top += 1
        if i == ')' or i == '}':
            if top == -1:
                return 0
            elif stack[top] == '(':
                stack.pop()
                top -= 1
            elif stack[top] == '{':
                stack.pop()
                top -= 1
            else:
                return 0
    if top != -1:
        return 0
    return 1

T = int(input())
for tc in range(1, T + 1):
    a = input()
    print(f'#{tc} {judge_bracket(a)}')