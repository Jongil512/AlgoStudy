# [[5000,120,30,1000], [3000,80,40,2000]], 150

# 기본요금, 기본시간, 추가시간, 추가요금

# 결과값 : 최소요금

def solution (passes,minutes):
    min_pay = 100000000
    for i in range(len(passes)):
        have_to_pay = 0
        base_fee, base_min, add_min, add_fee = passes[i]
        if minutes <= base_min:
            have_to_pay += base_fee
        else:
            have_to_pay += base_fee
            rest_min = minutes - base_min
            pay_cnt = rest_min // add_min + 1
            have_to_pay += pay_cnt * add_fee
            if have_to_pay <= min_pay:
                min_pay = have_to_pay
        
    answer = min_pay
    return answer

print(solution([[5000,120,30,1000], [3000,80,40,2000]], 150))