import sys
sys.stdin = open('4408_input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    s, e = map(int, input().split())
    print(s, e)