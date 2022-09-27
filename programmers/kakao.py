def cell_update(cell, r, c, word):
    cell[r][c] = word

def cell_update_change(cell, word1, word2):
    for i in range(50):
        for j in range(50):
            if cell[i][j] == word1:
                cell[i][j] == word2

def cell_merge(cell, r1, c1, r2, c2):
    if cell[r1][c1]:
        cell[r2][c2] = cell[r1][c1]
    else:
        cell[r1][c1] = cell[r2][c2]

def cell_unmerge(cell, r1, c1):
    for i in range(50):
        for j in range(50):
            if cell[i][j] == cell[r1][c1]:
                if i != r1 or j != c1:
                    cell[i][j] = ''

def cell_print(answer, cell, r1, c1):
    answer.append(cell[r1][c1])


def solution(commands):
    answer = []

    merged = [[]]

    N = 50
    cell = [([''] * N) for _ in range(N)]

    for command in commands:
        if command[:2] == 'UP':
            if len(command.split()) == 4:
                com, r, c, word = command.split()
                cell_update(cell, int(r), int(c), word)
            else:
                com, word1, word2 = command.split()
                cell_update_change(cell, word1, word2)

        elif command[:2] == 'ME':
            com, r1, c1, r2, c2 = command.split()
            cell_merge(cell, int(r1), int(c1), int(r2), int(c2))

        elif command[:2] == 'UN':
            com, r1, c1 = command.split()
            cell_unmerge(cell, int(r1), int(c1))

        else:
            com, r1, c1 = command.split()
            cell_print(answer, cell, int(r1), int(c1))

    return answer

commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant"
            , "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]

print(solution(commands))