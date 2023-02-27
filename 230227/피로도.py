from itertools import permutations

def solution(k, dungeons):
    answer = 0
    # 완전탐색을 위해 순열 생성
    ways = list(permutations(dungeons))

    for way in ways:
        # 소모 피로도를 빼며 비교하기 위해 재설정
        total = k
        # 최대 입장 가능 던전
        max_d = 0
        for i in range(len(dungeons)):
            # 남은 피로도가 필요 피로도 이상이면
            if way[i][0] <= total:
                # 소모 피로도 차감
                total -= way[i][1]
                # 입장 가능 던전 +1
                max_d = i + 1
            else:
                break
        # answer와 비교 후 큰 값을 재할당
        if max_d > answer:
            answer = max_d
    return answer