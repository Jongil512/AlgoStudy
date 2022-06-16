# 30

def mirco_30():
    num = sorted(N, reverse=True)
    # 0이 들어있지 않으면 존재 x
    if '0' not in num:
        return -1
    else:
        # 각 자릿수의 합이 3의 배수가 아니면 존재 x
        ssum = 0
        for i in num:
            ssum += int(i)
        if ssum % 3:
            return -1
        else:
            ans = ''.join(num)

    return ans

N = input()
print(mirco_30())
