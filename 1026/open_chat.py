def solution(records):
    tmp_logs = []
    logs = []
    match = {}
    user = []

    for record in records:
        devide = record.split(' ')
        if devide[0] == 'Enter':
            tmp_logs.append(f'{devide[1]}님이 들어왔습니다.')
            match[devide[1]] = devide[2]
            user.append(devide[1])
        elif devide[0] == 'Leave':
            tmp_logs.append(f'{devide[1]}님이 나갔습니다.')
            user.append(devide[1])
        else:
            match[devide[1]] = devide[2]

    for i in range(len(tmp_logs)):
        tmp_logs[i] = tmp_logs[i].replace(user[i], match[user[i]])

    return tmp_logs