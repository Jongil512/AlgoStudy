import sys

def solution(fees, records):
    records_split = []

    for rec in records:
        records_split.append(list(rec.split(' ')))

    # print(records_split)

    final_fee = {}

    while records_split:
        total_fee = 0
        first = records_split.pop(0)
        car_num = first[1]

        in_h = int(first[0][:2])
        in_m = int(first[0][3:])
        out_h = 0
        out_m = 0

        stay_h = 0
        stay_m = 0
        stay_time = 0

        for i in range(len(records_split)):
            if records_split[i][1] != car_num:
                continue
            if records_split[i][2] == 'IN':
                continue
            if records_split[i][2] == 'OUT':
                out_h = int(records_split[i][0][:2])
                out_m = int(records_split[i][0][3:])

                stay_h = out_h - in_h

                if out_m - in_m <= 0:
                    stay_h -= 1
                    stay_m = in_m + 60 - out_m
                else:
                    stay_m = out_m - in_m

                stay_time = stay_h * 60 + stay_m

                if stay_time <= fees[0]:
                    total_fee = fees[1]
                else:
                    if (stay_time - fees[0]) % fees[2] != 0:
                        total_fee = fees[1] + (((stay_time - fees[0]) // fees[2]) + 1) * fees[3]
                    else:
                        total_fee = fees[1] + ((stay_time - fees[0]) // fees[2]) * fees[3]

                if records_split[i][1] in final_fee:
                    final_fee[records_split[i][1]] += total_fee
                else:
                    final_fee[records_split[i][1]] = total_fee
                records_split.pop(i)
                first = []
                break
        if first:
            out_h = 23
            out_m = 59

            stay_time = (out_h - in_h) * 60 + out_m - in_m

            if stay_time <= fees[0]:
                total_fee = fees[1]
            else:
                if (stay_time - fees[0]) % fees[2] != 0:
                    total_fee = fees[1] + (((stay_time - fees[0]) // fees[2]) + 1) * fees[3]
                else:
                    total_fee = fees[1] + ((stay_time - fees[0]) // fees[2]) * fees[3]

            if records_split[0][1] in final_fee:
                final_fee[records_split[0][1]] += total_fee
            else:
                final_fee[records_split[0][1]] = total_fee

    answer = []

    new_fee = sorted(final_fee)
    for fee in new_fee:
        answer.append(fee[1])

    return answer


fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
a = 1
print(solution(fees, records))
