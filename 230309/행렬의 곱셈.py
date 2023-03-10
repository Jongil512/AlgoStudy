def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    # arr1의 행
    for i in range(len(arr1)):
        # arr1의 열 / arr2의 행
        for j in range(len(arr1[0])):
            # arr2의 열
            for k in range(len(arr2[0])):
                answer[i][k] += arr1[i][j] * arr2[j][k]

    return answer