import sys
sys.stdin = open('5948_input.txt')

def game_735():
    ans = []
    # 부분집합 생성 후 ans에 추가
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if arr[i] + arr[j] + arr[k] not in ans:
                    ans.append(arr[i] + arr[j] + arr[k])
    ans.sort()
    # 정렬 후 뒤에서 5번째 수 출력
    return ans[-5]

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)
    print(f'#{tc} {game_735()}')