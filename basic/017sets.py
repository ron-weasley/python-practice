setA = {"Harry Potter", "The Hobbit", "Fantastic Beast lol"}
setB = {"The Lord of the Rings", "The Hobbit"}

print(setA)
setA.remove("Fantastic Beast lol")
print(setA)
setA.add("Fantastic Beast")
print(setA)

# A and B but not A intersection B
print (setA.symmetric_difference(setB))
# symmetric_difference_update updates set

print('union : ', setA.union(setB))
# set_update takes union and update set

print('A intersection B : ', setA.intersection(setB))
# intersection_update updates set

print('A-B : ', setA.difference(setB))
# difference_update() updates set A with the set difference of A-B.
setA.difference_update(setB)
print(setA)

print (setA.isdisjoint(setB))
print (setA.issubset(setB))
print (setA.issuperset(setB))

