def solution(genres, plays):
    answer = []
    album = {}
    cnt = {}

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        # album 내에 genre 키값이 있다면 재생 횟수와 idx 추가
        # 존재하지 않으면 추가
        if genre in album:
            album[genre].append((play, idx))
        else:
            album[genre] = [(play, idx)]

        # cnt 내에 genre 키값이 있다면 재생 횟수 더해줌
        if genre in cnt:
            cnt[genre] += play
        else:
            cnt[genre] = play

    # 총 재생횟수를 기준으로 정렬한 리스트의 k값
    for (k, v) in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
        # album dic 내 k의 values를 재생횟수 기준으로 내림차순한 리스트를 슬라이싱
        for (p, i) in sorted(album[k], key=lambda x: x[0], reverse=True)[:2]:
            # 정답 리스트에 idx 추가
            answer.append(i)

    return answer