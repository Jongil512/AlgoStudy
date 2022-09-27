import sys
sys.stdin = open('11767_input.txt')

def baby_gin():
    flag = 0
    for i in range(6):
        player1.append(arr[i * 2])
        player2.append(arr[i * 2 + 1])
    for k in range(6):
        p1_visit[player1[k]] += 1
        p2_visit[player2[k]] += 1
        if max(p1_visit) == 3:
            flag = 1
            return flag
        if k >= 2:
            for j in range(8):
                if p1_visit[j] >= 1 and p1_visit[j+1] >= 1 and p1_visit[j + 2] >= 1:
                    flag = 1
                    return flag
        if max(p2_visit) == 3:
            flag = 2
            return flag
        if k >= 2:
            for j in range(8):
                if p2_visit[j] >= 1 and p2_visit[j+1] >= 1 and p2_visit[j + 2] >= 1:
                    flag = 2
                    return flag
    return flag

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    player1 = []
    player2 = []
    p1_visit = [0] * 10
    p2_visit = [0] * 10
    print(f'#{tc} {baby_gin()}')