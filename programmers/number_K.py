def solution(array, commands):
    answer = []
    i = j = k = 0
    for order in range(len(commands)):
        i = commands[order][0]
        j = commands[order][1]
        k = commands[order][2]
        new_lst = array[i-1:j]
        new_lst.sort()
        ans = new_lst[k-1]
        answer.append(ans)
    return answer


#   array = [1, 5, 2, 6, 3, 7, 4]
#   commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
#   return = [5, 6, 3]