def solution(numbers):

    # stack을 활용해 풀이
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        # 스택이 비어있지 않고 (아직 큰 수를 찾지 못한 수)
        # 스택의 가장 뒷 인덱스에 해당하는 numbers의 수가 현재 numbers[i]보다 작으면 반복
        while stack and numbers[stack[-1]] < numbers[i]:
            # 해당 인덱스에 해당하는 answer의 수를 numbers[i]로 변경
            answer[stack.pop()] = numbers[i]
        # 반복이 끝나거나 스택이 비어있다면 스택에 인덱스 추가
        stack.append(i)

    return answer