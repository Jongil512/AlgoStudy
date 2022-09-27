T = int(input())

s = 0

for tc in range(1, T + 1):
    if tc % 2 != 0:
        s += tc
    else:
        s -= tc
    print(f'#{tc} {s}')

    # s = s + tc if tc % 2 else s - tc