def solution(s):
    # set 차집합 사용을 위해 set으로 초기화
    answer = set()
    # 튜플 내 원소들을 split을 통해 분리
    tup_lst = list(s[2:-2].split('},{'))
    # 람다식을 이용해 원소의 길이를 오름차순으로 정렬
    tup_lst.sort(key=lambda x: len(x))
    rst = []

    for tup in tup_lst:
        # set 차집합 사용을 위해 리스트의 원소를 set으로 치환
        a = set(list(map(int, tup.split(','))))
        # set 차집합으로 비교한 원소를 결과 리스트에 담기
        rst = rst + list(set.difference(a, answer))
        # 담은 원소는 다음에 비교할 answer에 추가
        answer = a

    return rst
