# 1
# 효율성 테스트 3,4 실패
# 최대 O(n^2)이라 느리다
def solution(phone_book):
    for i in range(len(phone_book)):
        n = len(phone_book[i])
        for j in range(len(phone_book)):
            if len(phone_book[j]) < n or i == j:
                continue
            if phone_book[j][:n] == phone_book[i]:
                return False
    return True

# 2
def solution(phone_book):
    # sort는 길이 상관없이 첫 번째 인덱스를 기준으로 정렬된다
    # 11, 119, 119453, 15, 18340 ...
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        n = len(phone_book[i])
        # startswith() 보다 그냥 슬라이싱으로 비교하는 게 좀 더 빠르게 나왔다
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True