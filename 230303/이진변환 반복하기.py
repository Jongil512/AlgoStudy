def solution(s):
    cnt, n = 0, 0
    while s != 1:
        cnt += 1
        num = s.count('1')
        n += len(s) - num
        s = bin(num)[2::]
        if s == '1':
            return [cnt, n]