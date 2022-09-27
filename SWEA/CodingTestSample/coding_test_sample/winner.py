# ["lion:tiger", "lion:tiger", "lion:tiger", "lion:super", "super:tiger", "tiger:lion] , 4
# point = 4
#     승    패
# 1) lion tiger     lion이 tiger 처음 승!  4/1 -> 4
# 2) lion tiger     lion이 tiger 2번째 승!  4/2 -> 2
# 3) lion tiger     lion이 tiger 3번째 승!  4/3 -> 2 무조건 올림
# 4) lion super    lion이 super 1번째 승 4/1 -> 4
# 5) super tiger    super가 tiger 1번째 승 4/1 ->4 
# 6) tiger lion    tiger가 lion 1번째승 4/1 -> 4

# lion -> 4+2+2+4 12점
# super -> 4점
# tiger -> 4점

# 결과값 'lion'
# 점수가 같을경우 다승 -> 사전순(abc > abd)

def solution(results,p):
    N = len(results)
    teams = []
    # teams에 팀들 추가
    for i in range(N):
        for j in range(len(results[i])):
            if results[i][j] == ':':
                win = results[i][:j]
                lose = results[i][j+1:]
                if win not in teams:
                    teams.append(win)
                if lose not in teams:
                    teams.append(lose)
    print(teams)
    
    visi
    winner, loser = map(visited.index)

    answer = ''
    return answer

solution(["lion:tiger", "lion:tiger", "lion:tiger", "lion:super", "super:tiger", "tiger:lion"] , 4)