def solution(n):
    num = bin(n).count('1')
    while True:
        n += 1
        b2 = bin(n)
        if num == b2.count('1'):
            return n