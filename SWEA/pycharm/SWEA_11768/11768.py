import sys
sys.stdin = open('11768_input.txt')

# def merge(L, R):
#     # 두 개의 정렬된 리스트를 하나의 정렬된 리스트로 만들어서 반환
#     result = []
#
#     # 병합과정
#     # 1. 각각의 최솟값들 ( 가장 왼쪽 값 )을 비교해서 더 작은 요소를 결과에 추가
#     # 2. 두 리스트에 요소가 없어질 때까지 계속 반복
#     while L or R:
#         # 두 리스트가 모두 존재하면
#         if L and R:
#             if L[0] <= R[0]:
#                 result.append(L.pop(0))
#             else:
#                 result.append(R.pop(0))
#         # 왼쪽 리스트만 존재
#         # 하나씩 붙이는 방법
#         elif L:
#             result.append(L.pop(0))
#         # 한 번에 붙이는 방법 (나머지를 뒤에 붙임)
#         # result.extend(L)
#         # L.clear()
#         # 오른쪽 리스트만 존재
#         elif R:
#             result.append(R.pop(0))
#
#     return result

def merge_sort(a):
    global cnt
    # basis part
    if len(a) == 1:
        return a

    # 문제를 절반으로 나누어서 각 별도의 정렬 실행

    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        L = merge_sort(left)     # 마지막 1개 남을 떄까지 분할 후 리턴
        R = merge_sort(right)

        if L[-1] > R[-1]:
            cnt += 1

        i = j = 0
        res = []
        while i != len(L) and j != len(R):
            if L[i] < R[j]:
                res.append(L[i])
                i += 1
            else:
                res.append(R[j])
                j += 1

        if j != len(R):
            return res + R[j:]
        else:
            return res + L[i:]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)       # 비파괴 메서드
    print(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')