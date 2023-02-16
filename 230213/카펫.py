## 1차
def solution(brown, yellow):
    answer = []

    # 세로의 길이는 가로의 길이보다 같거나 작으므로 갈색의 양 모서리를 제거하고 나누기 2를 하면 세로 크기의 최대값
    a = (brown - 4) // 2

    # 세로의 길이를 1부터 시작해 a까지 반복
    for i in range(1, a + 1):
        # 세로 * 가로 == yellow가 되는 값을 찾음
        if i * (a - i) == yellow:
            answer.append(a - i + 2)
            answer.append(i + 2)
            break
    return answer

## 2차