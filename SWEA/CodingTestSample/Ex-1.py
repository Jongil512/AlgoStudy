def solution(T, time):
    if T == 1:
        return 0
    rest_time = [0] * len(time)
    for i in range(len(time)):
        while time[i] > T:
            time[i] = time[i] % T
        if time[i] != 0:
            rest_time[i] = (T-time[i])
    return max(rest_time)

T = 30 # 1 output 25 0
time = [20, 40, 65, 110]
print(solution(T, time))




#  1 2 3 5 2 4 7 4 5 6 7 8 9