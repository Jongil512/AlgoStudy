import sys
sys.stdin = open('11878_input.txt')

def forth(arr):
    top = -1
    stack = []
    for i in range(N):
        if arr[i].isdigit():
            stack.append(arr[i])
            top += 1
        elif arr[i] == '.':
            if top == 0:
                return int(stack.pop())
            else:
                return 'error'
        else:
            if top <= 0:
                return 'error'
            else:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                top -= 2
                if arr[i] == '+':
                    stack.append(op1 + op2)
                    top += 1
                elif arr[i] == '-':
                    stack.append(op1 - op2)
                    top += 1
                elif arr[i] == '*':
                    stack.append(op1 * op2)
                    top += 1
                else:
                    if op1 == 0 or op2 == 0:
                        return 'error'
                    else:
                        stack.append(op1 // op2)
                        top += 1
    return stack[top]

T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input().split()))
    N = len(arr)
    print(f'#{tc} {forth(arr)}')