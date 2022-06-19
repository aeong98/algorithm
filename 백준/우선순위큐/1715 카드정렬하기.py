import heapq

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

sum = 0
# 그 때마다 가장, 작은 카드 묶음 두개를 뽑아 A+B 비교 진행
for i in range(n-1):
    cmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, cmp)
    sum += cmp
print(sum)
