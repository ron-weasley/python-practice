# Dictionary - similar to hash map and mutable
dir1 = dict()
dir2 = {}

dir1["name"] = "Lord of the Rings"
dir1["genre"] = "Fantasy, Adventure"

dir2["name"] = "The" + " Hobbit"
dir2["genre"] = "High fantasy, Juvenile fantasy"

print (dir1)
dir1["name"] = "The Lord of the Rings"
print (dir1)
print (dir2)

print ("name" in dir1)

for index, key in enumerate(dir1):
    print(index, " ", key, " : ", dir1[key])
