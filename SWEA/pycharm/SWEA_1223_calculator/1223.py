import sys
sys.stdin = open('1223_input.txt')

def claculator2(a, n):
    top = -1
    stack = []
    ans_list = []
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(n):
        if a[i] in num_list:
            ans_list.append(a[i])
        elif a[i] == '+':
            if len(stack) != 0:
                while stack[top] == '+' or stack[top] == '*':
                    ans_list.append(stack.pop())
                    top -= 1
                    if top == -1:
                        break
            stack.append(a[i])
            top += 1
        elif a[i] == '*':
            if len(stack) != 0:
                while stack[top] == '*':
                    ans_list.append(stack.pop())
                    top -= 1
                    if top == -1:
                        break
            stack.append(a[i])
            top += 1

    while top > -1:
        ans_list.append(stack.pop())
        top -= 1

    for i in range(len(ans_list)):
        if ans_list[i] in num_list:
            stack.append(ans_list[i])
            top += 1
        else:
            b = int(stack[top])
            stack.pop()
            top -= 1
            a = int(stack[top])
            stack.pop()
            top -= 1
            if ans_list[i] == '+':
                stack.append(a + b)
                top += 1
            else:
                stack.append(a * b)
                top += 1
        if len(stack) == 1 and i == len(ans_list) - 1:
            return stack[0]

T = 10
for tc in range(1, T+1):
    N = int(input())
    sent = input()
    print(f'#{tc} {claculator2(sent, N)}')
