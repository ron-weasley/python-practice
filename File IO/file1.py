from itertools import islice

f = open('test.txt', 'r')
print(f.read(), '\n')

with open('test.txt', 'r') as f:
    for line in islice(f, 2):
        print(line, end="")

