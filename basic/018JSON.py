import json

data1 = '{"movie1":"Harry Potter", "movie2":"Fantastic Beast"}'
data2 = '{"movie2":"The Hobbit", "movie1":"The Lord of the Rings"}'

jsonData1 = json.loads(data1)
jsonData2 = json.loads(data2)
jsonstr1= json.dumps(jsonData1, sort_keys=True, indent=3)

print(jsonData1)
print(json.dumps(jsonData2, sort_keys=True, indent=3)) # object to strings

print(type(data1), type(jsonData1), type(jsonstr1))
print(jsonData1["movie1"])

with open("test1.json") as f:
    jsonData3 = json.load(f)

print(jsonData3)

with open("test1.json", "w") as f:
    json.dump(jsonData3, f, indent =4)
