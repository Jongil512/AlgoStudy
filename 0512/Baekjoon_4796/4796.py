i = 0
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    i += 1
    M = V // P
    can_use = L * M
    least = V - (M * P)
    if least <= L:
        can_use += least
    else:
        can_use += L
    print(f'Case {i}: {can_use}')