def solution(array, commands):
    answer = []
    for order in range(len(commands)):
        i = commands[order][0]
        j = commands[order][1]
        k = commands[order][2]
        new_lst = array[i-1:j]
        new_lst.sort()
        ans = new_lst[k-1]
        answer.append(ans)
    return answer

array = list(map(int, input().split()))
commands = [list(map(int, input().split())) for _ in range(3)]
print(solution(array, commands))

'''
1 5 2 6 3 7 4
2 5 3
4 4 1
1 7 3
'''