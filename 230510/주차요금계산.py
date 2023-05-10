import math

def solution(fees, records):
    answer = []
    cars = {}
    total = {}

    def calFee(fees, time):
        if time <= fees[0]:
            return fees[1]
        fee = fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
        return fee

    def toMinute(time):
        h, m = time.split(':')
        return int(h) * 60 + int(m)

    for record in records:
        time, carNum, isIn = record.split()
        if isIn == "IN":
            cars[carNum] = time
            if carNum not in total:
                total[carNum] = 0
        if isIn == "OUT":
            total[carNum] += toMinute(time) - toMinute(cars[carNum])
            cars[carNum] = 0

    for k, v in cars.items():
        if v:
            inTime = toMinute(v)
            outTime = toMinute("23:59")
            total[k] += (outTime - inTime)

    new_total = sorted(total.items(), key=lambda x:x[0])
    for v in new_total:
        answer.append(calFee(fees, v[1]))

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))