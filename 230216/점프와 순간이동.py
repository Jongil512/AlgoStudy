def solution(n):
    jump = 1

    while n > 1:
        jump += n % 2
        n //= 2

    return jump

# def solution(n):
#     return bin(n).count('1')