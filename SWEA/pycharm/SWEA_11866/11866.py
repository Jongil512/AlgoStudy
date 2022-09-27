import sys
sys.stdin = open('11866_input.txt')

def count_str(a, b):
    new_list = []
    # 중복 제거
    for i in a:
        if i not in new_list:
            new_list.append(i)
    # 최대 카운트 초기화
    max_cnt = 0
    # 중복 제거한 리스트에서 하나씩 꺼내 비교
    for item in new_list:
        # 카운트 초기화
        cnt = 0
        for j in range(len(b)):
            if item == b[j]:
                cnt += 1
                # 카운트 최댓값 갱신
                if cnt > max_cnt:
                    max_cnt = cnt
    return max_cnt

T = int(input())
for tc in range(1, T + 1):
    str1, str2 = [input() for _ in range(2)]
    print(f'#{tc} {count_str(str1, str2)}')