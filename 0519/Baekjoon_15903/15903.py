# 카드합체놀이

def func():
    cnt = 0
    while cnt < M:
        nums.sort()
        num_sum = nums[0] + nums[1]
        nums[0] = nums[1] = num_sum
        cnt += 1
    return sum(nums)

N, M = map(int, input().split())
nums = list(map(int, input().split()))
print(func())