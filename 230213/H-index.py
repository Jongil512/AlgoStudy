# H번 인용된 논문의 개수가 H개 이상, 나머지 논문이 H번 이하 인용되었다면 h-index = H
# H의 최댓값은 총 논문의 개수
def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)

    # 인용된 논문의 개수가 증가하면 인용된 횟수도 함께 증가함
    # i += 1
    for i in range(n):
        # 논문의 개수보다 인용된 횟수가 적어지는 순간 범위를 벗어남
        # ex) 6번째 논문의 인용 횟수가 1이라면 6은 H-index가 될 수 없음
        # [6, 6, 6, 6, 6, 1] -> 5
        # [3, 3, 3, 3, 3, 3] -> 3
        # [10, 9, 7, 6, 3, 3, 2, 1] -> 4
        if i+1 > citations[i]:
            return i
    return n