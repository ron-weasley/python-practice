with open('test.txt') as f1:
    with open('testA.txt', 'w') as f2:
        data = f1.read()
        f2.write(data)

f = open('test.txt') # default mode = read / 'r'
print(f.closed)
f.close()
print(f.closed)