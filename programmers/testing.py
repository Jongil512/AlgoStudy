def cal_fee(final_fee, total_time, fees):
    for key, value in total_time.items():

        if value <= fees[0]:
            total_fee = fees[1]
        else:
            if (value - fees[0]) % fees[2] != 0:
                total_fee = fees[1] + (((value - fees[0]) // fees[2]) + 1) * fees[3]
            else:
                total_fee = fees[1] + ((value - fees[0]) // fees[2]) * fees[3]

        if key in final_fee:
            final_fee[key] += total_fee
        else:
            final_fee[key] = total_fee


def solution(fees, records):
    records_split = []

    for rec in records:
        records_split.append(list(rec.split(' ')))

    final_fee = {}
    total_time = {x[1]: 0 for x in records_split}

    while records_split:
        first = records_split.pop(0)
        car_num = first[1]

        in_h = int(first[0][:2])
        in_m = int(first[0][3:])

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
                    stay_m = out_m + 60 - in_m
                else:
                    stay_m = out_m - in_m

                stay_time = stay_h * 60 + stay_m

                total_time[records_split[i][1]] += stay_time

                records_split.pop(i)
                first = []
                break

        if first:
            out_h = 23
            out_m = 59

            stay_time = (out_h - in_h) * 60 + out_m - in_m

            total_time[first[1]] += stay_time

    cal_fee(final_fee, total_time, fees)

    answer = []
    new_fee = sorted(final_fee.items())
    for fee in new_fee:
        answer.append(fee[1])

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
a = 1
print(solution(fees, records))