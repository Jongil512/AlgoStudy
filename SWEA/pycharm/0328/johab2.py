'''
for i1: 0 -> N - R + 0
    for i2: i1 + 1 -> N - R + 1
        for i3: i2 + 1 -> N - R + 2
'''
a = [1, 2, 3, 4]
N = len(a)
R = 3
for i in range(0, N - R + 1):                   # 4-3+1 = 2
    for j in range(i + 1, N - R + 2):           # 4-3+2 = 3
        for k in range(j + 1, N - R + 3):       # 4-3+3 = 4
            print(a[i], a[j], a[k])