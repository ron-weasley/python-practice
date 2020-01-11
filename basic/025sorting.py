# 1- insort
import bisect
# Sample list
my_list = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
print("Original List:")
print(my_list)
sorted_list = []
for i in my_list:
    # position = bisect.bisect(sorted_list, i)
    bisect.insort(sorted_list, i)
print("Sorted List:")
print(sorted_list)

# 2- sort
lis = [12, 124, 5654, 234, 34, 65, 0]
print(sorted(lis))

# 3- insertion point
import bisect
def index(a, x):
    # i = bisect.bisect_right(a, x)
    # i = bisect.bisect_left(a, x)
    i = bisect.bisect(a, x)
    return i
    
a = [1,2,4,7]
print(index(a, 6))
print(index(a, 3))
