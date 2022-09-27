def dc():
    for i in range(1, N):
        if arr[0][1] > arr[i][1] and arr[0][2] > arr[j][2]:
            arr[0][0] += 1


        # for j in range(i + 1, N):
        #     if arr[i][1] > arr[j][1] and arr[i][2] > arr[j][2]:
        #         cnt += 1
        #         arr[j][0] = cnt
        #     elif arr[i][1] < arr[j][1] and arr[i][2] < arr[j][2]:
        #         cnt += 1
        #         arr[i][0] = cnt

N = int(input())
arr = [[1] + list(map(int, input().split())) for _ in range(N)]
print(arr)
dc()
for i in range(N):
    print(arr[i][0], end=' ')