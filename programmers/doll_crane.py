def solution(board, moves):
    N = len(board[0])

    answer = 0
    q = []

    for move in moves:
        for i in range(N):
            if board[i][move - 1]:
                if q:
                    if q[-1] == board[i][move - 1]:
                        q.pop()
                        answer += 2
                    else:
                        q.append(board[i][move - 1])
                else:
                    q.append(board[i][move - 1])
                board[i][move - 1] = 0
                break

    return answer


#   board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
#   moves = [1,5,3,5,1,2,1,4]
#   answer = 4