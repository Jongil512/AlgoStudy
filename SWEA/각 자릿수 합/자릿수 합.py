T = int(input())

for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    sum = 0
    for n in a:
        while n > 10:
            sum += n % 10
            n = n // 10
        print(sum)
