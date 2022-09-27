import sys
sys.stdin = open('1221_input.txt')

def change_num(arr, n):
    num_dict = {'ZRO' : 0,
                'ONE' : 1,
                'TWO' : 2,
                'THR' : 3,
                'FOR' : 4,
                'FIV' : 5,
                'SIX' : 6,
                'SVN' : 7,
                'EGT' : 8,
                'NIN' : 9
                }
    cnt_list = [0] * 10
    # 딕셔너리와 같은 숫자의 인덱스 카운팅
    for i in range(n):
        cnt_list[num_dict[arr[i]]] += 1

    # 누적합
    for i in range(1, len(cnt_list)):
        cnt_list[i] = cnt_list[i] + cnt_list[i-1]

    sorting_list = [0] * n
    for i in range(len(sorting_list)-1, -1, -1):
        sorting_list[cnt_list[num_dict[arr[i]]]-1] = arr[i]
        cnt_list[num_dict[arr[i]]] -= 1

    return ' '.join(sorting_list)

T = int(input())
for tc in range(1, T + 1):
    bin1, bin2 = map(str, input().split())
    words = list(map(str, input().split()))
    n = len(words)
    print(f'#{tc} {change_num(words, n)}')