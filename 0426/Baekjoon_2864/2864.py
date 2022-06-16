import copy

A, B = map(str, input().split())

max_A = copy.deepcopy(A)
max_B = copy.deepcopy(B)
min_A = copy.deepcopy(A)
min_B = copy.deepcopy(B)
max_AB = 0
min_AB = 0

if '5' in A:
    max_A = A.replace('5', '6')
if '5' in B:
    max_B = B.replace('5', '6')
max_AB = int(max_A) + int(max_B)

if '6' in min_A:
    min_A = A.replace('6', '5')
if '6' in min_B:
    min_B = B.replace('6', '5')
min_AB = int(min_A) + int(min_B)

print(min_AB, max_AB)