import random
import secrets
import os
# struct module to convert bytes into the format you want
import struct

x = [1980, "lol", "harry", "Erebor"]
print(random.choice(x))
random.shuffle(x)
print(x)
print(random.sample(x, 2))
print(int(random.random() * 10))  # between 0 to 10
print(random.randint(10, 100))  # between 10 to 100 inclusing 10 & 100
print(random.randrange(200, 300, 5))
random.seed(4)  # sam erandom number every time
print(random.randrange(200, 300, 5))

# The cryptographically secure random generator generates random data
# using synchronization methods to ensure
# that no two processes can obtain the same data at the same time
secretGenerator = secrets.SystemRandom()
print(secretGenerator.randint(9, 99))
print(secretGenerator.randrange(9, 99, 3))
print(secretGenerator.sample(x, 2))

# to cryptographically secure the random generator
print(struct.unpack('i', os.urandom(4))) 
# for random integer unpack requires a buffer of 4 bytes
print(struct.unpack('I', os.urandom(4))) 
# for unsigned random integer unpack requires a buffer of 4 bytes

#  short-2,  unsigned short-2
print(struct.unpack('h', os.urandom(2))) 
print(struct.unpack('H', os.urandom(2))) 

#  float-4,  un-signed integer-8 (include float + integer)
print(struct.unpack('f', os.urandom(4))) 
print(struct.unpack('d', os.urandom(8))) 

print(struct.unpack('c', os.urandom(1))) 
