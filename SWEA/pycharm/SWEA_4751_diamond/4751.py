import sys
sys.stdin = open('4751_input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    N = len(word)
    a = '..#..'
    b = '.#.#.'
    if N == 1:
        print(a)
        print(b)
        print(f'#.{word}.#')
        print(b)
        print(a)
    else:
        print(a[:4] * N + '.')
        print(b[:4] * N + '.')
        for i in word:
            print(f'#.{i}.', end='')
        print('#')
        print(b[:4] * N + '.')
        print(a[:4] * N + '.')