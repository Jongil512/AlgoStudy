import heapq
# heap = [7, 2, 5, 3, 4, 6]
# heapq.heapify(heap) # 한 번에 힙으로 변환 (min heap)
# print(heap)
# heapq.heappush(heap, 1)
# print(heap)
# while heap:
#     print(heapq.heappop(heap), end=' ')
###########################################
# max heap으로 하는 방법
temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, -temp[i])
print(heap2)
while heap2:
    print(heapq.heappop(heap2) * -1, end=' ')