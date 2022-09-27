T = int(input())

for tc in range(1, T + 1):
    a = input()
    while len(a) > 1:
        if a[0] == a[-1]:
            a = a[1:-1]
        else:
            print(0)




    # for i in range(len(a) // 2):
    #     if a[i] != a[-i -1]:
    #         print(f'#{tc} 0')
    #         break
    #     if i == len(a) // 2 -1:
    #         print(f'#{tc} 1')
    #         break
