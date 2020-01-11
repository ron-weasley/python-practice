import heapq

h = [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]
print(heapq.nlargest(2, h))
print(heapq.nsmallest(3, h))

# minheap
a = [1, 6, 3, 9, 5, 9]
heapq.heapify(a)
print(a)
heapq.heappop(a)
heapq.heappush(a, 8)
heapq.heappushpop(a, 5)
print(a)
print(heapq.nlargest(1,a))
print(a)
heapq.heapreplace(a,10)
print(heapq.nlargest(1,a))

# maxheap
a = [1, 6, 3, 9, 5, 9]
heapq._heapify_max(a)
print(a)
heapq._heappop_max(a)
print(a)