# Lists (can be used for stack or array operations, its mutable)
a = [0]
a.append("lol0")
a.append("lol1")
print(a)
a.pop()
a.insert(2, 0)
print (a, "\nno. of time \'0\' appeared: ",a.count(0))
a.clear()
print (a)
a=[1,5,3]
b=[2,3,6]
print(set(a)-set(b))
print(a.index(5), "\n\n")

# Tupple (immutable)
b = ("hell", " rises")
print (b)
for x in b: print (x, end="")
print ("\n", b.__contains__("hell"))