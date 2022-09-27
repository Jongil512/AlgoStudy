T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number_list = list(map(int, input()))
    total = 0
    for num in number_list:
        total += num

n = total / (len(number_list))

print(f'#{test_case} {n}')
        
    