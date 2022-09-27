import sys
sys.stdin = open('10828_input.txt')

def push(n):
    stack.append(int(arr[1]))
    top += 1

def size():
    return len(stack)

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0

def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[top]

def pop():
    if top == -1:
        return -1
    else:
        return stack.pop()
        top -= 1



T = int(input())
stack = []
top = -1
for tc in range(1, T+1):
    arr = list(input().split())
    if arr[0] == 'push':
        push(int(arr[1]))
    else:


    # if arr[0] == 'push':
    #     stack.append(int(arr[1]))
    #     top += 1
    # elif arr[0] == 'top':
    #     if top == -1:
    #         print('-1')
    #     else:
    #         print(stack[top])
    # elif arr[0] == 'size':
    #     print(len(stack))
    # elif arr[0] == 'empty':
    #     if len(stack) == 0:
    #         print('1')
    #     else:
    #         print('0')
    # else:
    #     if top == -1:
    #         print('-1')
    #     else:
    #         print(stack[top])
    #         stack.pop()
    #         top -= 1