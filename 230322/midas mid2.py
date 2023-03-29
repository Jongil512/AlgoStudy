from itertools import combinations
def solution(n, m, names, authors):
    answer = 0
    dic = {name:float('inf') for name in names}
    dic['erdos'] = 0
    for author in authors:
        target = float('inf')
        for au in author:
            if dic[au] < target:
                target = dic[au]
        for au in author:
            if dic[au] > target:
                dic[au] = target + 1

    cnt = 0
    for v in dic.values():
        if v < 6:
            cnt += 1

    for k in range(n-cnt, n):
        for j in range(k+1):
            answer += len(list(combinations(range(k), j)))
    return answer


# 헝가리의 수학자 에르되시 팔(Paul Erdös, 1913-1996)은 평생동안 1500여 편에 달하는 논문을 저술했고, 대부분의 논문을 다른 학자와 공동으로 저술했다. 에르되시 수(Erdös Number)는 공동연구 네트워크에서 에르되시와 몇 단계를 거쳐 연결되어 있는지를 나타내는 수이다.
#
# 에르되시 수는 아래와 같이 재귀적으로 정의된다.
#
# 1. 에르되시의 에르되시 수는 0이다.
# 2. 에르되시와 공동 작업을 한 사람의 에르되시 수는 1이다.
# 3. 임의의 사람 P의 에르되시 수는 (P와 공동 작업을 한 사람들의 에르되시 수의 최솟값) + 1이다.
# 4. 이러한 공저자 관계가 없는 사람의 에르되시 수는 무한대로 정의한다.
#
# 필즈상을 받고 싶은 수학자 시루(siroo)는 2016년까지의 모든 필즈상 수상자들의 에르되시 수가 6 이하라는 이야기를 듣게 되었다. 아직 에르되시 수가 무한대인 시루는 논문을 단 한 편만 저술해서 에르되시 수를 6 이하로 만들려고 한다.
#
# 논문들의 공저자 관계가 주어졌을 때, 시루의 에르되시 수가 6 이하가 되는 공동 작업 동료 집합의 경우의 수를 구해보자.
#
# 입력
# n: 공동연구 네트워크에 포함된 학자의 수 (1 ≤ n ≤ 200,000)
# m: 공동연구 네트워크에 포함된 논문의 수 (1 ≤ m ≤ 200,000)
#
# names[i]: 공동연구 네트워크에 포함된 학자의 이름 (1 ≤ 한 논문에 참여한 학자의 수 ≤ N),
# 학자의 이름은 알파벳 소문자 5글자로 구성되어 있고, 서로 다르다.
# erdos는 공동연구 네트워크에 항상 포함되며, siroo는 포함되지 않는다.
#
# authors[i]: i번째 논문에 참여한 학자의 이름 (1 ≤ 각 논문에 참여한 학자의 수의 총합 ≤ 200,000)
# 한 논문에 참여한 학자의 이름은 서로 다르다.
# 공동연구 네트워크에 포함된 모든 학자는 한 편 이상의 논문에 참여했다.
#
# 입출력 예제 1
# n, m, names, authors, return
print(solution(8, 8, ["justi","cehui","jhnah","erdos","aaaaa","bbbbb","ccccc","ddddd"], [["erdos","justi"],["justi","cehui"],["cehui","jhnah"],["jhnah","aaaaa"],["aaaaa","bbbbb"],["bbbbb","ccccc"],["ccccc","ddddd"],["ccccc","ddddd"]]))
# 8, 8, ["justi","cehui","jhnah","erdos","aaaaa","bbbbb","ccccc","ddddd"], [["erdos","justi"],["justi","cehui"],["cehui","jhnah"],["jhnah","aaaaa"],["aaaaa","bbbbb"],["bbbbb","ccccc"],["ccccc","ddddd"],["ccccc","ddddd"]], 252