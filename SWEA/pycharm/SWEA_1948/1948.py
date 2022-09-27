import sys
sys.stdin = open('cal_date_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    # 각 월을 일수 별로 리스트화
    day31_list = [1, 3, 5, 7, 8, 10, 12]
    day30_list = [4, 6, 9, 11]
    day28_list = [28]
    # 값 초기화
    day1 = 0
    day2 = 0
    # 1월인 경우와 아닌 경우로 나눔
    if arr[0] != 1 and arr[2] != 1:
        for i in range(1, arr[0]):
            # 각 월별 일수를 합산
            if i in day31_list:
                day1 += 31
            elif i in day30_list:
                day1 += 30
            else:
                day1 += 28

        for i in range(1, arr[2]):
            if i in day31_list:
                day2 += 31
            elif i in day30_list:
                day2 += 30
            else:
                day2 += 28
    elif arr[0] == 1 and arr[2] != 1:
        for i in range(1, arr[2]):
            if i in day31_list:
                day2 += 31
            elif i in day30_list:
                day2 += 30
            else:
                day2 += 28
    else: # 둘 다 1월인 경우 일수를 값에 할당
        day1 = arr[1]
        day2 = arr[3]
    day1 += arr[1]
    day2 += arr[3]
    result = day2 - day1 + 1
    print(f'#{tc} {result}')