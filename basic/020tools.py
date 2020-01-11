import itertools

print(list(itertools.permutations([1, 5, 6])))

a = [1, 5, 3]
b = [2, 3, 6]
c = [[1], [2, 3], [1, 4, 55, 56], [356]]
print(list(itertools.accumulate(a)))
print(list(itertools.product(a, b)))
# print(list(itertools.product(a, b, a)))
print(list(itertools.chain(*c)))
